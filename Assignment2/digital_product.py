from product import Product


class DigitalProduct(Product):
    def __init__(self, item_id, item_name, base_price, discount):
        super().__init__(item_id, item_name, base_price)
        self.discount = discount

    def calculate_price(self):
        discount_amount = self.base_price * (self.discount / 100)
        return int(self.base_price - discount_amount)

    def get_info(self):
        return "{} (Digital, {}% OFF) -> PKR {}".format(
            self.item_name, self.discount, self.calculate_price()
        )
