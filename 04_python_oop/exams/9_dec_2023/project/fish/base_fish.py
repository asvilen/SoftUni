from abc import ABC, abstractmethod


class BaseFish(ABC):
    _INVALID_NAME_MSG = "Fish name should be determined!"
    _MIN_POINTS = 1
    _MAX_POINTS = 10
    _INVALID_POINTS_MSG = "Points should be a value ranging from 1 to 10!"

    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError(self._INVALID_NAME_MSG)
        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value: float):
        if not (self._MIN_POINTS <= value <= self._MAX_POINTS):
            raise ValueError(self._INVALID_POINTS_MSG)
        self.__points = value

    @abstractmethod
    def fish_details(self):
        pass