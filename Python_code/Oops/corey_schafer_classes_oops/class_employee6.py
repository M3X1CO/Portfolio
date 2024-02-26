

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

    def __init__(self, first, last, pay, prog_lang):
        # uses parent class to get first, last, and pay
        super().__init__(first, last, pay)
        # can also call Employee same as super
        # Employee().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    # dont use muteable objects for employees=[] for example
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        # print(mgr_1.__dict__)
        print(f"Supervising Manager {mgr_1.first} {mgr_1.last}")
        print('Supervised Employees')
        for emp in self.employees:
            print('-->', emp.full_name())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
emp_1 = Employee('Howard', 'Felix', 50000)
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(dev_1.email)
print(dev_1.prog_lang)

print()
print(emp_1.email)
print(emp_1.pay)

print()
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(emp_1)
print()
mgr_1.print_emps()
print()
mgr_1.remove_emp(emp_1)
mgr_1.print_emps()

print()
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print()
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
