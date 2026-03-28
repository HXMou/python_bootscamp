from functions import input_employees_date, input_managers_date, list_employee_position, list_subordinate, balance_display

managers = []
employees = []


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
                print("List of employee on this posotion: ")
                list_employee_position(employees)

            elif manage_action == "subordinates":
                list_subordinate(managers, employees)

            elif manage_action == "balance":
                print(f"Total salary is {balance_display(managers, employees)}")

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