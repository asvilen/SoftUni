from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    _aircon = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity / (self.fuel_consumption + self._aircon) >= distance:
            self.fuel_quantity -= distance * (self.fuel_consumption + self._aircon)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    _aircon = 1.6
    FUEL_COEF = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity / (self.fuel_consumption + self._aircon) >= distance:
            self.fuel_quantity -= distance * (self.fuel_consumption + self._aircon)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_COEF


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)