

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"

    def email(self):
        return f"{self.first}.{self.last}@email.com"


emp_1 = Employee('Corey', 'Schafer')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email())
print(emp_1.full_name())
