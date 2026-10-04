product_name = input("Enter Product Name: ")
product_price = float(input("Enter Product Price: "))
product_quantity = float(input("Enter Product Quantity: "))


def calculate_discount(price, quantity):
    subtotal = price * quantity
    discount = 0.10 * subtotal
    final_total = subtotal - discount
    return subtotal, discount, final_total

subtotal, discount, final_total = calculate_discount(product_price, product_quantity)

def print_receipt(name, subtotal, discount, final_total):
    print("\n--- Receipt ---")
    print(f"Product Name: {name}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Final Total: ${final_total:.2f}")
    print("----------------")

print_receipt(product_name, subtotal, discount, final_total)

def input_student_data():
    name = input("Enter Student Name: ")
    marks = float(input("Enter Student Marks: "))
    return name, marks

def process_student_grade(name, marks):
        
        if marks >= 80:
            grade = 'A'
        elif marks >= 70:
            grade = 'B'
        elif marks >= 60:
            grade = 'C'
        else:
            grade = 'F'
        return name, grade

def print_student_grade(name, grade):
    print(f"Student Name: {name}, Grade: {grade}")

input_name, input_marks = input_student_data()
student_name, student_grade = process_student_grade(input_name, input_marks)
print_student_grade(student_name, student_grade)
