from models import Employee, Manager

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

    return new_employee

def list_subordinate(managers, employees):
    print("List of manager's subordinates")
    m_first_name = input("Enter manager's first name: ")
    m_last_name = input("Enter manger's last name: ")

    for manager in managers:
        if manager.f_name == m_first_name and manager.l_name == m_last_name:
            for employee in employees:
                if employee.department == manager.department:
                    print(employee)

def list_employee_position(employees):
    position = input("Enter position name: ")
    for employee in employees:
        if employee.position == position:
            print(employee)

def balance_display(managers, employees):
    salary_emplpoyees = 0.0
    for employee in employees:
        salary_emplpoyees += employee.salary
    salary_managers = 0.0
    for manager in managers:
        salary_managers += manager.salary
                
    total_salary = salary_managers+salary_emplpoyees
    return total_salary