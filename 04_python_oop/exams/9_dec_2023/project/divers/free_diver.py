from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    _INITIAL_OXYGEN_LEVEL = 120
    _OXYGEN_REDUCTION_PERCENTAGE = 0.6

    def __init__(self, name: str):
        super().__init__(name, self._INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        oxy_to_remove = round(time_to_catch * self._OXYGEN_REDUCTION_PERCENTAGE)
        if self.oxygen_level < oxy_to_remove:
            oxy_to_remove = self.oxygen_level
        self.oxygen_level -= oxy_to_remove

    def renew_oxy(self):
        self.oxygen_level = self._INITIAL_OXYGEN_LEVEL

    def __str__(self):
        return f"FreeDiver: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, " \
               f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"