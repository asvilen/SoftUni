from project.computer_types.computer import Computer, ram_gen


class Laptop(Computer):
    _comp_type = 'laptop'
    _available_processors = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200,
    }
    max_ram = 64

