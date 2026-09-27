def get_employee_details():
    name = input("Employee Name: ")
    basic_salary = float(input("Basic salary: "))
    allowance = float(input("Allowance: "))
    tax_rate = float(input("Tax rate (%): "))
    return name, basic_salary, allowance, tax_rate


def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    return gross_salary * (tax_rate / 100)


def calculate_net_salary(gross_salary, tax_amount):
    return gross_salary - tax_amount


def display_salary_slip(name, gross, tax, net):
    print("\n----- Salary Slip -----")
    print("Employee Name :" ,name)
    print("Gross Salary  : ", gross)
    print("Tax Deducted  :" ,tax)
    print("Net Salary    : ", net)


name, basic, allowance, tax_rate = get_employee_details()
gross = calculate_gross_salary(basic, allowance)
tax = calculate_tax(gross, tax_rate)
net = calculate_net_salary(gross, tax)
display_salary_slip(name, gross, tax, net)