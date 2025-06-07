from dynamixel_port import DynamixelPort


class Controller:
    """
    A class to represent a controller

    Attributes:
        dxl (DynamixelPort): The dynamixel port
        motor_id (int): The motor id
        min (int): The minimum position of the controller
        max (int): The maximum position of the controller
        current (int): The current of the motor
        position (int): The position of the motor
    """

    def __init__(self, motor_id, min, max, dxl: DynamixelPort):
        self.dxl = dxl
        self.motor_id = motor_id
        self.min = min
        self.max = max
        self.current = 0
        self.position = 0

    def get_pos(self, motor_ids, multi_turn=True):
        """
        Get the position of the motor

        Args:
            motor_ids (list): The motor ids
            multi_turn (bool): Whether the motor is multi-turn

        Returns:
            list: The position of the motor
        """
        return self.dxl.get_pos(motor_ids, multi_turn)

    def get_min(self):
        """
        Get the minimum position of the motor

        Returns:
            int: The minimum position of the motor
        """
        return self.min

    def get_max(self):
        """
        Get the maximum position of the motor

        Returns:
            int: The maximum position of the motor
        """
        return self.max

    def go_to_position(self, position):
        """
        Move the controller to a specific position

        Args:
            position (int): The position to move the controller to in percent
        """
        controller_pos = (
            ((position / 100) * (self.max - self.min) + self.min) / 360 * 4095
        )
        self.dxl.set_goal_pos(self.motor_id, controller_pos)

    def move_to_touch(self, max_time_duration=2):
        """
        Move the controller to touch an object

        Args:
            max_time_duration (int): The maximum time duration to touch the object
        """
        pass

    def map_position(self):
        """
        Map the controller position to the finger position
        """
        pass

    def move_to_position(self, position):
        """
        Move the controller to a specific position

        Args:
            position (int): The position to move the controller to in percent
        """
