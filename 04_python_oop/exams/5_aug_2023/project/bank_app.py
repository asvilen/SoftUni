from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    loan_types = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan,
    }
    client_types = {
        'Student': Student,
        'Adult': Adult,
    }
    loan_appropriateness = {
        'Student': 'StudentLoan',
        'Adult': 'MortgageLoan',
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type in self.loan_types:
            loan_obj = self.loan_types[loan_type]()
            self.loans.append(loan_obj)
            return f"{loan_type} was successfully added."
        raise Exception("Invalid loan type!")

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.client_types:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        client_obj = self.client_types[client_type](client_name, client_id, income)
        self.clients.append(client_obj)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan_to_grant = loan
                break

        for client in self.clients:
            if client.client_id == client_id:
                if loan_type == self.loan_appropriateness[client.__class__.__name__]:
                    self.loans.remove(loan_to_grant)
                    client.loans.append(loan_to_grant)
                    return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."
                break

        raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        does_not_exist = True
        has_loans = False

        for client in self.clients:
            if client.client_id == client_id:
                client
                does_not_exist = False
                has_loans = True if len(client.loans) > 0 else False
                break

        if does_not_exist:
            raise Exception("No such client!")

        if has_loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                counter += 1
        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_income = sum([client.income for client in self.clients])
        loans_count_granted_to_clients = len([loan for client in self.clients for loan in client.loans])
        granted_sum = sum([loan.amount for client in self.clients for loan in client.loans])
        loans_count_not_granted = len([loan for loan in self.loans])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        client_interest_rates = [client.interest for client in self.clients]
        if len(client_interest_rates) == 0:
            avg_client_interest_rate = 0
        else:
            avg_client_interest_rate = sum(client_interest_rates) / len(client_interest_rates)
        info = [
            f"Active Clients: {len(self.clients)}",
            f"Total Income: {total_income:.2f}",
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}",
            f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}",
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        ]
        return "\n".join(info)
