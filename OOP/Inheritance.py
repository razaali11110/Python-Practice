# Inheritance is the technique to get all the attributes of the parent class into the child class
# This is done by passing the parameters in the child class of the parent class

# class Fruit:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavour = flavor


# class Apple(Fruit):  # inherited from the parent class of Fruits
#     pass

# class Bannana(Fruit):  # inherited from the parent class of Fruits
#     pass


# apple1 = Apple("Red", "Sweet")
# banana = Bannana("White", "Very Sweet")

# print(apple1.color, banana.flavour)

# creating a parent class

class Employee:
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def increase_raise(cls, class_raise):
        cls.raise_amount = class_raise

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    @classmethod
    def raise_developer(cls, amount):
        cls.raise_amount = amount


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    @classmethod
    def raise_manager(cls, amount):
        cls.raise_amount = amount

    def all_employees(self):
        for i in self.employees:
            print(i.fullname())

    def add_employee(self, empl):
        if empl not in self.employees:
            self.employees.append(empl)

    def remove_employee(self, empl):
        if empl in self.employees:
            self.employees.remove(empl)

