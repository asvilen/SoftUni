from abc import ABC, abstractclassmethod
from math import log2


def ram_gen(max_ram):
    for power in range(1, int(log2(max_ram)) + 1):
        yield 2 ** power, power

# [print(i) for i in ram_gen(64)]


class Computer(ABC):
    _comp_type = ''
    _available_processors = {}
    max_ram = 128
    _ram_map = {ram: power for ram, power in ram_gen(max_ram)}

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self.__model = value


    def configure_computer(self, processor: str, ram: int):
        if processor not in self._available_processors.keys():
            raise ValueError(f"{processor} is not compatible with {self._comp_type} {self.manufacturer} {self.model}!")
        self.processor = processor
        if ram not in self._ram_map.keys():
            raise ValueError(f"{ram}GB RAM is not compatible with {self._comp_type} {self.manufacturer} {self.model}!")
        self.ram = ram
        self.price = self._available_processors[processor] + 100 * self._ram_map[ram]
        return f"Created {self.__repr__()} for {self.price}$."


    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"


