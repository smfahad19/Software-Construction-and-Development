class Order:
    def __init__(self, order_no):
        self.order_no = order_no
        self.items_list = []

    def add_item(self, item):
        self.items_list.append(item)
        print("Success: '{}' added to cart.".format(item.item_name))

    def get_total_price(self):
        bill = 0
        for item in self.items_list:
            bill += item.calculate_price()
        return int(bill)

    def print_bill(self):
        print("------ Cart Summary (Order #{}) --------".format(self.order_no))
        print("==========================================")
        if not self.items_list:
            print("Cart is empty.")
            return
        count = 1
        for item in self.items_list:
            print("{}. {}".format(count, item.get_info()))
            count = count + 1

        print("------------------------------------------")
        print("Subtotal Amount: PKR {}".format(self.get_total_price()))

    def checkout(self, payment_option):
        self.print_bill()
        bill_amount = self.get_total_price()

        if bill_amount > 0:
            payment_option.pay_bill(bill_amount)
            print("\nCheckout Completed Successfully!\n")
        else:
            print("\nCheckout Failed: Cart is empty.")
