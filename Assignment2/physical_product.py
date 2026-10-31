from product import Product


class PhysicalProduct(Product):
    def __init__(self, item_id, item_name, base_price, shipping_fee):
        super().__init__(item_id, item_name, base_price)
        self.shipping_fee = shipping_fee

    def calculate_price(self):
        return self.base_price + self.shipping_fee

    def get_info(self):
        return "{} (Physical) -> PKR {}".format(
            self.item_name, self.calculate_price()
        )
