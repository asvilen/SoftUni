from abc import ABC, abstractmethod


class BaseLoan(ABC):
    initial_interest_rate = 0
    initial_amount = 0

    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self):
        pass

