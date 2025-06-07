import time
from dynamixel_port import DynamixelPort
from linear_interpolation import LinearInterpolation

from controller import Controller


class Finger:
    """
    A class to represent a finger

    Attributes:
        dxl (DynamixelPort): The dynamixel port
        controller (Controller): The controller
        name (str): The name of the finger
        min (int): The minimum position of the finger
        max (int): The maximum position of the finger
        motor_id (int): The motor id
        touch_current (int): The touch current
        current (int): The current of the motor
        position (int): The position of the motor
    """

    def __init__(
        self,
        name,
        min,
        max,
        motor_id,
        touch_current,
        port: DynamixelPort,
        controller: Controller,
    ):
        self.dxl = port
        self.controller = controller
        self.name = name
        self.min = min
        self.max = max
        self.motor_id = motor_id
        self.touch_current = touch_current
        self.current = 0
        self.position = 0

    def move_to_position(self, position):
        """
        Move the finger to a specific position

        Args:
            position (int): The position to move the finger to in percent
        """
        finger_pos = ((position / 100) * (self.max - self.min) + self.min) / 360 * 4095
        self.dxl.set_goal_pos(self.motor_id, finger_pos)

    def map_position(self, translation=1):
        """
        Map the finger position to the controller position
        """
        controller_pos_raw = self.controller.get_pos(
            [self.controller.motor_id], multi_turn=False
        )[0]
        controller_pos = controller_pos_raw / 4095 * 360
        controller_min = self.controller.get_min()
        controller_max = self.controller.get_max()

        self.move_to_position(
            ((controller_pos - controller_min) / (controller_max - controller_min))
            * 100
            * translation
        )

    def move_to_touch(self, max_time_duration=2):
        """
        Move the finger to touch an object

        Args:
            max_time_duration (int): The maximum time duration to touch the object
        """
        kf_1 = [0]
        kf_2 = [100]
        keyframes = [kf_1, kf_2]
        durations = [max_time_duration]
        start_time = time.time()
        lin = LinearInterpolation(keyframes, durations)

        while time.time() - start_time < max_time_duration:
            time_in_loop = time.time() - start_time
            values = lin.get_values_for_time(time_in_loop)
            self.move_to_position(values[0])
            current = self.dxl.get_current([self.motor_id])[0]
            if abs(current) > abs(self.touch_current):
                break

    def get_current(self):
        """
        Get the current of the motor
        """
        self.current = self.dxl.get_current([self.motor_id])[0]
        return self.current

    def get_position(self):
        """
        Get the position of the motor
        """
        self.position = self.dxl.get_pos([self.motor_id], multi_turn=False)[0]
        return self.position
