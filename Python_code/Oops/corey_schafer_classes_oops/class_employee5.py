

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


class Developer(Employee):
    raise_amount = 1.10


dev_1 = Developer('Corey', 'Schafer', 50000)
emp_1 = Employee('Howard', 'Felix', 50000)


# print(help(Developer)) # great info here on corey_schafer_classes_oops
# print(dev_1.email)
# print(dev_2.email)

# changing a subclass raise amount
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
