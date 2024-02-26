

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Corey', 'Schafer')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)

# trying to build a setter... @full_name.setter
print()
emp_1.full_name = 'Howard Felix'

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)

print()
del emp_1.full_name
print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)
