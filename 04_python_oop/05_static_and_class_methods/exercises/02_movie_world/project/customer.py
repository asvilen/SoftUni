class Customer:
    def __init__(self, name, age, customer_id):
        self.name = name
        self.age = age
        self.id = customer_id
        self.rented_dvds = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
                f"rented DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})")


# the_customer = Customer("Giotere", 51, 3)
# print(the_customer)

