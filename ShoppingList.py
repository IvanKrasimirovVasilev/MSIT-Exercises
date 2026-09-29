class ShoppingList:

    def __init__(self, product_list):
        self._products = {}

        for product_name in product_list:
            current_amount = self._products.get(product_name, 0)
            self._products[product_name] = current_amount + 1

    def total_amount(self):
        return sum(self._products.values())

    def __len__(self):
        return len(self._products)

    def __contains__(self, product_name):
        return product_name in self._products

    def __add__(self, other):
        new_products = self._products.copy()

        for product_name, amount in other._products.items():
            current_amount = new_products.get(product_name, 0)
            new_products[product_name] = current_amount + amount

        return new_products

    def add_product(self, product_name, amount):
        current_amount = self._products.get(product_name, 0)
        self._products[product_name] = current_amount + amount

    def __mul__(self, multiplier):
        new_shoppinglist = ShoppingList([])
        for product_name, amount in self._products.items():
            new_shoppinglist.add_product(product_name, amount * multiplier)
        return new_shoppinglist


    def __str__(self):
        return f"My shopping list has {len(self._products)} different products and {self.total_amount()} total amount."

new_list = ShoppingList(["Milk", "Milk", "Eggs"])
list2 = ShoppingList(["Juice", "Eggs"])

print(new_list)
print(len(new_list))
print("Milk" in new_list)
print("Pizza" in new_list)

doubled_list = new_list * 2

print(doubled_list)