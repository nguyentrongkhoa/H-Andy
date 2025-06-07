try:
    from dynamixel_port import DynamixelPort
    print("Test successful")
except Exception as e:
    print("Test failed: ", e)
