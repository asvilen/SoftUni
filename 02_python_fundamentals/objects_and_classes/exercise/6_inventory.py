class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.left_capacity = self.__capacity
        self.items = []

    def add_item(self, item: str):
        if self.left_capacity > 0:
            self.left_capacity -= 1
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items_list = ', '.join(self.items)
        return f"Items: {items_list}.\nCapacity left: {self.left_capacity}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
