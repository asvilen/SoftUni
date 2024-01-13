from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    _DEFAULT_TIME_TO_CATCH = 90

    def __init__(self, name: str, points: float):
        super().__init__(name, points, self._DEFAULT_TIME_TO_CATCH)

    def fish_details(self):
        return f"PredatoryFish: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"