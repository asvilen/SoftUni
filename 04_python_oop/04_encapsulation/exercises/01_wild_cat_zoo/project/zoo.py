from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def has_budget(self, price):
        return self.__budget >= price

    def has_capacity(self):
        return len(self.animals) + 1 <= self.__animal_capacity

    def add_animal(self, animal: Animal, price):
        if not self.has_capacity():
            return "Not enough space for animal"

        if not self.has_budget(price):
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if  len(self.workers) + 1 > self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_worker_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_worker_salaries:
            self.__budget -= total_worker_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_animal_care = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_money_for_animal_care:
            self.__budget -= total_money_for_animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        info = f"You have {len(self.animals)} animals"
        animal_types = [animal.__class__.__name__ for animal in self.animals]
        for animal_type in ['Lion', 'Tiger', 'Cheetah']:
            amount = animal_types.count(animal_type)
            info += f"\n----- {amount} {animal_type}s:\n"
            animals_info = [str(animal) for animal in self.animals if animal.__class__.__name__ == animal_type]
            info += "\n".join(animals_info)
        return info

    def workers_status(self):
        info = f"You have {len(self.workers)} workers"
        worker_types = [worker.__class__.__name__ for worker in self.workers]
        for worker_type in ['Keeper', 'Caretaker', 'Vet']:
            amount = worker_types.count(worker_type)
            info += f"\n----- {amount} {worker_type}s:\n"
            workers_info = [str(worker) for worker in self.workers if worker.__class__.__name__ == worker_type]
            info += "\n".join(workers_info)
        return info
