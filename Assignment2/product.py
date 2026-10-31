class Product:
    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name
        self.base_price = base_price

    def calculate_price(self):
        return self.base_price

    def get_info(self):
        return "{} -> PKR {}".format(self.item_name, self.calculate_price())
