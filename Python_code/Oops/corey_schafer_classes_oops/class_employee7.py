

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

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    # combine employee pay
    def __add__(self, other):
        return self.pay + other.pay

    # dunder len method
    def __len__(self):
        return len(self.full_name())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Howard', 'Felix', 60000)

# print(1 + 2)
# print('a' + 'b')

# does the same
# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))

# print(emp_1)

print(repr(emp_1))

print(str(emp_1))

# does the same
# print(emp_1.__repr__())
# print(emp_1.__str__())

print(emp_1 + emp_2)

print(len('test'))
# print('test'.__len__())

print(len(emp_1))
