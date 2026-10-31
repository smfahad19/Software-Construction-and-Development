class CardPayment:
    def __init__(self, card_num, owner_name):
        self.card_num = card_num
        self.owner_name = owner_name

    def pay_bill(self, total_amount):
        bank_fee = int(total_amount * 0.02)
        final_bill = int(total_amount + bank_fee)
        hidden_card = "****-****-****-{}".format(self.card_num[-4:])

        print("\n--- Card Payment Processing ---")
        print("Card Holder : {}".format(self.owner_name))
        print("Card Number : {}".format(hidden_card))
        print("Subtotal    : PKR {}".format(int(total_amount)))
        print("Card Fee 2% : PKR {}".format(bank_fee))
        print("Total Paid  : PKR {}".format(final_bill))
        print("Status      : Payment Successful!")
        return True
