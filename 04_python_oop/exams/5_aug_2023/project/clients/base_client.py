from abc import ABC, abstractmethod


class BaseClient(ABC):
    _client_id_number_of_characters = 10

    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Client name cannot be empty!")
        self.__name = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        if len(value) != self._client_id_number_of_characters:
            raise ValueError("Client ID should be 10 symbols long!")
        self.__client_id = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        if value <= 0:
            raise ValueError("Income must be greater than zero!")
        self.__income = value

    @abstractmethod
    def increase_clients_interest(self):
        pass

    # @abstractmetod
    # def __str__(self):
    #     return self.__name__