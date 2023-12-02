from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    initial_interest_rate = 3.5
    initial_amount = 50000.0

    def __init__(self):
        super().__init__(self.initial_interest_rate, self.initial_amount)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
