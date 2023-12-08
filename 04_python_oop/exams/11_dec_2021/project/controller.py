from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    _AVAILABLE_CARS = {
        'MuscleCar': MuscleCar,
        'SportsCar': SportsCar,
    }
    _MIN_RACE_PARTICIPANTS = 3

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self._AVAILABLE_CARS:
            self.__raise_if_car_exists(model)
            return self.__add_new_car(car_type, model, speed_limit)

    def create_driver(self, driver_name: str):
        if not self.__name_not_found(driver_name, self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        return self.__add_new_driver(driver_name)

    def create_race(self, race_name: str):
        if not self.__name_not_found(race_name, self.races):
            raise Exception(f"Race {race_name} is already created!")
        return self.__add_new_race(race_name)

    def add_car_to_driver(self, driver_name: str, car_type: str):
        self.__raise_if_driver_not_found(driver_name, self.drivers)
        if self.__car_not_found(car_type):
            raise Exception(f"Car {car_type} could not be found!")

        driver = self.__get_obj(driver_name, self.drivers)
        car = self.__get_available_car(car_type)
        car.is_taken = True

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

        driver.car = car
        return f"Driver {driver_name} chose the car {driver.car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        self.__raise_if_race_is_not_found(race_name, self.races)
        self.__raise_if_driver_not_found(driver_name, self.drivers)

        driver = self.__get_obj(driver_name, self.drivers)
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race = self.__get_obj(race_name, self.races)
        return self.__add_driver_to_race_if_possible(driver, race)


    def start_race(self, race_name: str):
        self.__raise_if_race_is_not_found(race_name, self.races)
        self.__raise_if_not_enough_participants(race_name)
        race = self.__get_obj(race_name, self.races)
        return self.__get_race_results(race)



    def __raise_if_car_exists(self, model):
        if model in [car.model for car in self.cars]:
            raise Exception(f"Car {model} is already created!")

    def __add_new_car(self, car_type, model, speed_limit):
        created_car = self._AVAILABLE_CARS[car_type](model, speed_limit)
        self.cars.append(created_car)
        return f"{car_type} {model} is created."

    def __add_new_driver(self, driver_name):
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def __add_new_race(self, race_name):
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def __car_not_found(self, car_type):
        if car_type not in self._AVAILABLE_CARS:
            return True
        if all([car.is_taken for car in self.cars]):
            return True
        return False

    def __get_available_car(self, car_type):
        return [car for car in self.cars if isinstance(car, self._AVAILABLE_CARS[car_type]) and not car.is_taken][-1]

    def __raise_if_driver_not_found(self, driver_name, drivers):
        if self.__name_not_found(driver_name, drivers):
            raise Exception(f"Driver {driver_name} could not be found!")

    def __raise_if_race_is_not_found(self, race_name, races):
        if self.__name_not_found(race_name, races):
            raise Exception(f"Race {race_name} could not be found!")

    def __raise_if_not_enough_participants(self, race_name):
        race = self.__get_obj(race_name, self.races)
        if len(race.drivers) < self._MIN_RACE_PARTICIPANTS:
            raise Exception(f"Race {race_name} cannot start with less than {self._MIN_RACE_PARTICIPANTS} participants!")

    @staticmethod
    def __name_not_found(name, obj_list):
        if name in [obj.name for obj in obj_list]:
            return False
        return True

    @staticmethod
    def __get_obj(obj_name, obj_list):
        return [obj for obj in obj_list if obj.name == obj_name][0]

    @staticmethod
    def __add_driver_to_race_if_possible(driver, race):
        if driver in [driver for driver in race.drivers]:
            return f"Driver {driver.name} is already added in {race.name} race."
        race.drivers.append(driver)
        return f"Driver {driver.name} added in {race.name} race."

    @staticmethod
    def __get_race_results(race):
        top_3_sl = sorted([driver.car.speed_limit for driver in race.drivers], reverse=True)[:3]
        results = []
        for sl in top_3_sl:
            for driver in race.drivers:
                if driver.car.speed_limit == sl:
                    driver.number_of_wins += 1
                    results.append(f"Driver {driver.name} wins the {race.name} race with a speed of {driver.car.speed_limit}.")
        return "\n".join(results)
