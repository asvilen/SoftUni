from abc import ABC, abstractmethod


class BaseService(ABC):
    _INVALID_NAME_MSG = "Service name cannot be empty!"
    _MAX_INVALID_CAPACITY = 0
    _INVALID_CAPACITY_MSG = f"Service capacity cannot be less than or equal to {_MAX_INVALID_CAPACITY}!"

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError(self._INVALID_NAME_MSG)
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= self._MAX_INVALID_CAPACITY:
            raise ValueError(self._INVALID_CAPACITY_MSG)
        self.__capacity = value

    @abstractmethod
    def details(self):
        pass