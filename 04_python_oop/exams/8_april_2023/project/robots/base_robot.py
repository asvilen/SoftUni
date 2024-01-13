from abc import ABC, abstractmethod


class BaseRobot(ABC):
    _EMPTY_NAME_MSG = "Robot name cannot be empty!"
    _EMPTY_KIND_MSG = "Robot kind cannot be empty!"
    _INVALID_PRICE = 0.0
    _INVALID_PRICE_MSG = f"Robot price cannot be less than or equal to {_INVALID_PRICE}!"

    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if self.__empty_str(value):
            raise ValueError(self._EMPTY_NAME_MSG)
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if self.__empty_str(value):
            raise ValueError(self._EMPTY_KIND_MSG)
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= self._INVALID_PRICE:
            raise ValueError(self._INVALID_PRICE_MSG)
        self.__price = value

    @abstractmethod
    def eating(self):
        pass

    @staticmethod
    def __empty_str(value):
        if value.strip() == "":
            return True
        return False