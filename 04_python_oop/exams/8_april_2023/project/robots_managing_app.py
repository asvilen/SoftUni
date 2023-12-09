from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    _SERVICES_MAP = {
        'MainService': MainService,
        'SecondaryService': SecondaryService,
    }
    _ROBOTS_MAP = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot,
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self._SERVICES_MAP:
            raise Exception("Invalid service type!")
        service_to_add = self._SERVICES_MAP[service_type](name)
        self.services.append(service_to_add)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self._ROBOTS_MAP:
            raise Exception("Invalid robot type!")
        robot_to_add = self._ROBOTS_MAP[robot_type](name, kind, price)
        self.robots.append(robot_to_add)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__get_obj(robot_name, self.robots)
        service = self.__get_obj(service_name, self.services)
        if self.__service_is_unsuitable(robot, service):
            return "Unsuitable service."
        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__get_obj(service_name, self.services)
        robot = self.__get_obj(robot_name, service.robots)
        if not robot:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__get_obj(service_name, self.services)
        [bot.eating() for bot in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__get_obj(service_name, self.services)
        bots = [bot for bot in service.robots]
        total_price = sum([bot.price for bot in bots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        info = []
        for service in self.services:
            info.append(service.details())
        return "\n".join(info)

    @staticmethod
    def __service_is_unsuitable(robot, service):
        if isinstance(robot, MaleRobot) and isinstance(service, SecondaryService):
            return True
        if isinstance(robot, FemaleRobot) and isinstance(service, MainService):
            return True
        return False

    @staticmethod
    def __get_obj(obj_name, obj_list):
        for obj in obj_list:
            if obj.name == obj_name:
                return obj
