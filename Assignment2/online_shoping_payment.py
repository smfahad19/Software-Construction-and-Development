from card_payment import CardPayment
from cash_on_delivery import CashOnDelivery
from digital_product import DigitalProduct
from order import Order
from physical_product import PhysicalProduct


def main():
    catalog = {
        "1": PhysicalProduct("P101", "Keyboard", 2500, 200),
        "2": DigitalProduct("D101", "E-Book", 1200, 10),
        "3": PhysicalProduct("P102", "Book", 800, 150),
        "4": DigitalProduct("D102", "Online Course", 3000, 15),
    }
    user_order = Order("1001")

    while True:
        print("\n==========================================")
        print("      ONLINE SHOPPING SYSTEM MENU         ")
        print("1. View Store Products")
        print("2. Add Product to Cart")
        print("3. View Cart Summary")
        print("4. Proceed to Checkout")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            print("\n--- AVAILABLE PRODUCTS ---")
            for product_id in catalog:
                print("{}. {}".format(product_id, catalog[product_id].get_info()))

        elif choice == "2":
            print("\n--- SELECT PRODUCT TO ADD ---")
            for product_id in catalog:
                print("{}. {}".format(product_id, catalog[product_id].item_name))

            num = input("\nEnter product number (1-4): ").strip()
            if num in catalog:
                user_order.add_item(catalog[num])
            else:
                print("Invalid choice.")

        elif choice == "3":
            user_order.print_bill()

        elif choice == "4":
            if not user_order.items_list:
                print("\nCart is empty! Add products first.")
                continue

            print("\n--- PAYMENT METHOD ---")
            print("1. Card Payment")
            print("2. Cash on Delivery")

            pay_choice = input("Select payment method (1-2): ").strip()

            if pay_choice == "1":
                name = input("Enter Card Holder Name: ").strip()
                card_num = input("Enter 16-Digit Card Number: ").strip()
                payment = CardPayment(card_num, name)
                user_order.checkout(payment)
                break

            elif pay_choice == "2":
                address = input("Enter Delivery Address: ").strip()
                payment = CashOnDelivery(address)
                user_order.checkout(payment)
                break
            else:
                print("Invalid payment choice.")

        elif choice == "5":
            print("\nExiting system.")
            break
        else:
            print("Invalid choice, enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
