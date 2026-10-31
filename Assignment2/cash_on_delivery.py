class CashOnDelivery:
    def __init__(self, address):
        self.address = address

    def pay_bill(self, total_amount):
        cod_charge = 150
        final_bill = int(total_amount + cod_charge)

        print("\n--- Cash on Delivery ---")
        print("Address     : {}".format(self.address))
        print("Subtotal    : PKR {}".format(int(total_amount)))
        print("COD Charge  : PKR {}".format(cod_charge))
        print("Collect Cash: PKR {}".format(final_bill))
        print("Status      : Order Placed (Pending Cash Collection)")
        return True
