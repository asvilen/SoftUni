from project.clients.base_client import BaseClient


class Adult(BaseClient):
    initial_interest_rate = 4.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.initial_interest_rate)

    def increase_clients_interest(self):
        self.interest += 2.0
