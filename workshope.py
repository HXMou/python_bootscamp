books = {
    "Harry Potter": 3,
    "The Lord of the rings": 5,
    "The Witcher": 10,
    "The catch in the rye": 4,
    "Glucose reolution": 2
}

history = list()

while True:
    command = input("Enter command: ").upper() #whatever input gonna change to UPPER case. 

    if command == "EXIT":
        print("Ending the program.")
        break
    elif command == "ADD":
        history.append(command)

        print("Add a book.\n")
        title = input("Enter book title: ")
        quatity = int(input("Enter quatity: "))
        if quatity > 0 :
            #books already have
            if title in books:
                books[title] += quatity
            else:
            #new books
                books[title] = quatity
        else:
            print("the quantity should be greater than 0.")

    elif command == "BORROW":
        history.append(command)

        print("Borrow a book. \n")
        title = input("Enter book title: ")
        quatity = int(input("Enter quatity to borrow: "))

        if quatity > 0 :
            #books already have
            if title in books and books[title] >= quatity:
                books[title] -= quatity
                print(f"Borrowed {quatity} \"{title}\" success.")
            else:
            #new books
                print(f"No enough \"{title}\" available.")
        else:
            print("the quantity should be greater than 0.")

    elif command == "BOOKS":
        history.append(command)

        print("Lists of books:\n")
        if books: #check firstly if book exists 
            for title, quatity in books.items():
                print(f"- \"{title}\":{quatity} pcs.")

    elif command == "AVAILABILITY":
        history.append(command)

        print("Check if the book is available.\n")
        title = input("Enter book title: ")
        if title in books:
            print(f"{books[title]} of {title} is available.")
        else:
            print(f"{title} is not available. ")

    elif command == "UNIQUE":
        history.append(command)

        print("Check the unique number of all titles:\n")
        unique_count = len(books)
        print(unique_count)

    elif command == "COUNT":
        history.append(command)

        print("Total number of books: ")
        print(sum(books.values()))

    elif command == "HELP":
        history.append(command)

        print("""List of available commands:
              """)
        
    elif command == "HISTORY":
        print("Commands history: \n")
        for item in history:
            print(item)

    else: 
        print("Unknown command. Type 'HELP' to see the list of commands.")