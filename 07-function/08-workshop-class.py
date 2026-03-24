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

managers = []
employees = []

def input_managers_date():
    first_name = input("Ebter first name: ")
    last_name = input("Enter last name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    new_manager = Manager(first_name, last_name, department, salary)

    return new_manager

def input_employees_date():
    first_name = input("Ebter first name: ")
    last_name = input("Enter last name: ")
    department = input("Enter department: ")
    position = input("Enter the position: ")
    salary = float(input("Enter salary: "))

    new_employee = Employee(first_name, last_name, department, position, salary)

    return new_manager

while True:
    action = input("What you want to do?: [create, manage, exit]").lower()

    if action == "exit":
        break

    elif action == "manage":
        while True:
            manage_action = input("What role you want to manage? [position, subordinates, balance, exit]").lower()
            if manage_action == "exit":
                break
            elif manage_action == "position":
                pass
            elif manage_action == "subordinates":
                print("List of manager's subordinates")
                m_first_name = input("Enter manager's first name: ")
                m_last_name = input("Enter manger's last name: ")

                for manager in managers:
                    if manager.f_name == m_first_name and manager.l_name == m_last_name:
                        for employee in employees:
                            if employee.department == manager.department:
                                print(employee)

            elif manage_action == "balance":
                pass

    elif action == "create":
        while True:
            create_action = input("What role you want to create? [Manager, Employee, exit]").lower()
            if create_action == "exit":
                break
            elif create_action == "manager":
                print("Adding new manager.")
                new_manager = input_managers_date()
                managers.append(new_manager)
            elif create_action == "employee":
                print("Adding new employee.")
                new_employee = input_employees_date()
                employees.append(new_employee)

    else: 
        print("Invalid action")

print("The end of the program.")