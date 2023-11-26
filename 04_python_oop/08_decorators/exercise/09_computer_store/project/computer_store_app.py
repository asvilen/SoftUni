from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    _valid_types = {
        'Desktop Computer': DesktopComputer,
        'Laptop': Laptop,
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self._valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        computer = self._valid_types[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((c for c in self.warehouse
                         if self.sell_is_possible(c, client_budget, wanted_processor, wanted_ram)), None)
        if not computer:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{computer} sold for {client_budget}$."

    @staticmethod
    def sell_is_possible(computer, client_budget, wanted_processor, wanted_ram):
        if computer.price <= client_budget \
            and computer.processor == wanted_processor \
                and computer.ram >= wanted_ram:
            return True
        return False


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))

# print(DesktopComputer._comp_type.title())
