from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    _INVALID_NAME_MSG = "Diver name cannot be null or empty!"
    _MIN_INVALID_OL = 0
    _INVALID_OXYGEN_LEVEL_MSG = "Cannot create diver with negative oxygen level!"

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = float(f"{0:.1f}")
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError(self._INVALID_NAME_MSG)
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value: float):
        if value < self._MIN_INVALID_OL:
            raise ValueError(self._INVALID_OXYGEN_LEVEL_MSG)
        if value == self._MIN_INVALID_OL:
            self.has_health_issue = True
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points += fish.points

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    @abstractmethod
    def __str__(self):
        pass