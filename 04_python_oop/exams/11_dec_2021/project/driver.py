from project.car.car import Car


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car: Car = None
        self.number_of_wins: int = 0

