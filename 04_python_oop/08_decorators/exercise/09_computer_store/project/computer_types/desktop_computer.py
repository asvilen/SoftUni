from project.computer_types.computer import Computer, ram_gen


class DesktopComputer(Computer):
    _comp_type = 'desktop computer'
    _available_processors = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5 - 12600K': 600,
        'Apple M1 Max': 1800,
    }

