from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    _DIVERS_MAP = {
        'FreeDiver': FreeDiver,
        'ScubaDiver': ScubaDiver,
    }
    _FISHES_MAP = {
        'PredatoryFish': PredatoryFish,
        'DeepSeaFish': DeepSeaFish,
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self._DIVERS_MAP:
            return f"{diver_type} is not allowed in our competition."
        if diver_name in [diver.name for diver in self.divers]:
            return f"{diver_name} is already a participant."

        diver = self._DIVERS_MAP[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self._FISHES_MAP:
            return f"{fish_type} is forbidden for chasing in our competition."
        if fish_name in [fish.name for fish in self.fish_list]:
            return f"{fish_name} is already permitted."

        fish = self._FISHES_MAP[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.__get_obj(diver_name, self.divers)
        fish = self.__get_obj(fish_name, self.fish_list)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            return self.__diver_missed(diver, fish)
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                return self.__diver_hits(diver, fish)
            else:
                return self.__diver_missed(diver, fish)
        else:
            return self.__diver_hits(diver, fish)

    def health_recovery(self):
        divers_with_health_issues = [diver for diver in self.divers if diver.has_health_issue]
        for diver in divers_with_health_issues:
            diver.has_health_issue = False
            diver.renew_oxy()
        return f"Divers recovered: {len(divers_with_health_issues)}"

    def diver_catch_report(self, diver_name: str):
        diver = self.__get_obj(diver_name, self.divers)
        info = [f"**{diver_name} Catch Report**"]
        info += [fish.fish_details() for fish in diver.catch]
        return "\n".join(info)

    def competition_statistics(self):
        info = ["**Nautical Catch Challenge Statistics**"]
        divers_dict = {len(diver.catch): diver.competition_points for diver in self.divers}
        divers_dict_ordered = list(sorted(divers_dict.items(), key=lambda x: (-x[1], x[0])))
        for catch_count, points in divers_dict:
            diver = self.__get_obj(diver_name, self.divers)
            if not diver.has_health_issue:
                info.append(str(diver))
        return "\n".join(info)

    @staticmethod
    def __get_obj(obj_name, obj_list):
        for obj in obj_list:
            if obj.name == obj_name:
                return obj

    @staticmethod
    def __diver_hits(diver, fish):
        diver.hit(fish)
        return f"{diver.name} hits a {fish.points}pt. {fish.name}."

    @staticmethod
    def __diver_missed(diver, fish):
        diver.miss(fish.time_to_catch)
        return f"{diver.name} missed a good {fish.name}."
