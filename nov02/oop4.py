class Employee:
    raise_amnt = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name} earns {self.salary}'

    def give_raise(self):
        self.salary = int(self.salary * self.raise_amnt)


class Developer(Employee):
    raise_amnt = 1.1

    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        return super().__str__() + f' and loves {self.prog_lang}'


class Boss(Employee):
    raise_amnt = 1.07


def main():
    emp1 = Employee('Anna', 'Jones', 55000)
    emp2 = Employee('John', 'Smith', 47000)
    dev1 = Developer('Sara', 'Andersen', 55000, 'Python')
    boss1 = Boss('Peter', 'Black', 60000)

    employees = [emp1, emp2, dev1, boss1]

    for emp in employees:
        if isinstance(emp, Boss):
            print(emp.first_name, 'is a Boss')
        else:
            print(emp.first_name, 'is not a Boss')
    # print(emp1)
    # print(emp2)
    # Employee.raise_amnt = 1.05
    # emp1.give_raise()
    # emp2.give_raise()
    # print(emp1)
    # print(emp2)
    # print(dev1)
    # dev1.give_raise()
    # print(dev1)

if __name__ == '__main__':
    main()
