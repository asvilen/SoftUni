from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    initial_interest_rate = 1.5
    initial_amount = 2000.0

    def __init__(self):
        super().__init__(self.initial_interest_rate, self.initial_amount)

    def increase_interest_rate(self):
        self.interest_rate += 0.2
