

class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Howard', 'Felix', 500000)

# Employee.set_raise_amt(1.06)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steven-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


# using class methods as alternative constructors
# can build like this or create an alternative constructor in @classmethod from_string above
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)
#
#
# print(new_emp_1.email)
# print(new_emp_1.pay)
