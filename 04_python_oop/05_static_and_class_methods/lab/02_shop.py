class Shop:
    _small_shop_capacity = 10

    def __init__(self, name, shop_type, capacity):
        self.name = name
        self.shop_type = shop_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, shop_type):
        return cls(name, shop_type, cls._small_shop_capacity)

    def add_item(self, item_name):
        if self.capacity == sum(item_value for item_value in self.items.values()):
            return f"Not enough capacity in the shop"

        if item_name not in self.items.keys():
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def _can_remove_amount(self, item_name, amount):
        return item_name in self.items \
            and self.items[item_name] >= amount

    def remove_item(self, item_name, amount):
        if not self._can_remove_amount(item_name, amount):
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            self.items.pop(item_name)
        return f"{amount} {item_name} removed from the shop"

    def __str__(self):
        return f"{self.name} of type {self.shop_type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
