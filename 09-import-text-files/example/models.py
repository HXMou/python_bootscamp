class Manager:
    def __init__(self, first_name, last_name, dep, salary):
        self.f_name = first_name
        self.l_name = last_name
        self.dep = dep
        self.salary = salary

class Employee: 
    def __init__(self, first_name, last_name, dep, postion, salary):
        self.f_name = first_name
        self.l_name = last_name
        self.dep = dep
        self.position = postion
        self.salary = salary

    def __str__(self):
        return f"{self.f_name} {self.l_name} {self.position} ({self.dep})"