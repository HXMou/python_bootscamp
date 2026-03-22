#   - 'balance': The program should prompt for an amount to add or subtract from the account.
#   - 'sale': The program should prompt for the name of the product, its price, and quantity. Perform necessary calculations and update the account and warehouse accordingly.
#   - 'purchase': The program should prompt for the name of the product, its price, and quantity. Perform necessary calculations and update the account and warehouse accordingly. Ensure that the account balance is not negative after a purchase operation.
#   - 'account': Display the current account balance.
#   - 'list': Display the total inventory in the warehouse along with product prices and quantities.
#   - 'warehouse': Prompt for a product name and display its status in the warehouse.
#   - 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range. If ‘from’ and ‘to’ are empty, display all recorder operations. Handle cases where 'from' and 'to' values are out of range.
#   - 'end': Terminate the program.


ava_command = ["BALANCE", "SALE", "PURCHASE", "ACCOUNT", "LIST", "WAREHOUSE", "REVIEW", "END"]
# use dict{"key", value}
total_balance = 100
inventory = {
    "APPLE": {"price": 2, "quantity": 10},
    "BANANA": {"price": 1.50, "quantity": 30},
    "KIWI": {"price": 5, "quantity": 10}
}
command_history = []

print('Available commands: \n')
for i in ava_command:
    print(f'- {i}')

while True:
    command = input("Enter your command: ").upper()

    if command in ava_command:
        command_history.append(command)

        if command == "END":
            print("Finish the programm. Bye.")
            break

        elif command == "BALANCE":
            amount = float(input("Enter the amount to add or subtract: "))
            total_balance += amount
            print(f"Current account balance: {total_balance}.")

        elif command == "SALE":
            s_pname = input("Product name: ").upper()
            s_pprice = float(input("Product price: "))
            s_pnum = int(input("Product quantity: "))
            if s_pname in inventory:
                    print(f"Found {s_pname} for sale.")
                    item = inventory[s_pname]
                    if s_pnum <= item["quantity"]:
                        item["quantity"] -= s_pnum
                        total_balance += s_pprice*s_pnum
                        print(f"Sold {s_pnum} {s_pname} for {s_pprice*s_pnum}. New account balance is {total_balance}.")
                    else:
                        print(f"No enough inventory for {s_pname}. Only have {item['quantity']}.")
            else:
                print("No such a product.")

        elif command == "ACCOUNT":
            print(f"Current account balance: {total_balance}.")
        
        elif command == "PURCHASE":
            p_pname = input("Purchase product name: ").upper()
            p_pprice = float(input("Purchase price: "))
            p_pnum = int(input("How many you want to purchase: "))
            if p_pnum*p_pprice <= total_balance:
                if p_pname in inventory:
                    item = inventory[p_pname]
                    print(f"Already has {item['quantity']} {p_pname}.")
                    inventory[p_pname] = {"price": p_pprice, "quantity": item["quantity"]+p_pnum}
                else:
                    print(f"Purchased a new product {p_pname} to inventory.")
                    inventory[p_pname] = {"price": p_pprice, "quantity": p_pnum}
                total_balance -= p_pnum*p_pprice
            else:
                print("No enough balance in accounbt to complete this purchase.")

        elif command == "LIST":
            for name, item in inventory.items():
                print(f"{name} with price {item['price']} eur per kg, quantity: {item['quantity']}.")

        elif command == "WAREHOUSE":
            product_name_to_check = input("Which prodct you want to check: ").upper()
            if product_name_to_check in inventory:
                product_status = inventory[product_name_to_check]
                print(f"{product_name_to_check} current price is {product_status['price']} eur per kg, remain inventory is {product_status['quantity']}.")
            else: 
                print(f"Invalid input! No product {product_name_to_check}.")
        
        elif command == "REVIEW":
            from_command = int(input("The from number: "))
            to_command = int(input("The to number: "))
            while True:
                if from_command <= to_command and to_command <= len(command_history) :
                    print("The list of previous commands:")
                    for i in range(from_command, to_command):
                        print(f"{command_history[i-1]}")
                    break
                else:
                    print("Invalid from and to range")
                    from_command = input("The from number: ")
                    to_command = input("The to number: ")

    else:
        print("Invalid command, please re-enter:")
        command = input("Enter your command: ").upper()