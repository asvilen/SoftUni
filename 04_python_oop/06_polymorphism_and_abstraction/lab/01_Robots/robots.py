class Robot:
    _sensor = 1

    def __init__(self, name):
        self.name = name

    @classmethod
    def sensors_amount(cls):
        return cls._sensor


class MedicalRobot(Robot):
    _sensor = 6


class ChefRobot(Robot):
    _sensor = 4


class WarRobot(Robot):
    _sensor = 12


def number_of_robot_sensors(robot: Robot):
    print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
