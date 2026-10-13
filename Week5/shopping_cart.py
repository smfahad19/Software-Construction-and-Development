"""A small example of a shopping cart.

Each cart has its own items list. add_item() stores each product's name,
price, and quantity, while calculate_total() returns the cart's total.
Keeping the list on each cart makes two cart instances independent.
"""

class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add_item(self, item_name, price, quantity):
        self.items.append((item_name, price, quantity))
        
    def calculate_total(self):
        total = 0
        for price, quantity in self.items:
            total += price * quantity
        return total
    
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item[0] != item_name]

cart1 = ShoppingCart()
cart1.add_item("Apple", 0.5, 4)
cart1.add_item("Banana", 0.3, 6)

cart2 = ShoppingCart()
cart2.add_item("Bread", 1.2, 2)
cart2.add_item("Milk", 2.0, 1)

print("Cart 1 total:", cart1.calculate_total())
print("Cart 2 total:", cart2.calculate_total())

