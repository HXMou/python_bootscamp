from utils import display_help, display_history, dispaly_volume_count, unique_book_title, availability_check, list_all_books, borrow_books, add_books, load_books

books = load_books()

history = list()

while True:
    command = input("Enter command: ").upper() #whatever input gonna change to UPPER case. 
    history.append(command)

    if command == "EXIT":
        print("Ending the program.")
        break
    
    elif command == "ADD":
        books = add_books(books)

    elif command == "BORROW":
        books = borrow_books(books)

    elif command == "LISTS":
        list_all_books(books)

    elif command == "AVAILABILITY":
        availability_check(books)

    elif command == "UNIQUE":
        unique_book_title(books)

    elif command == "COUNT":
        dispaly_volume_count(books)

    elif command == "HELP":
        display_help()
        
    elif command == "HISTORY":
        display_history()

    else: 
        print("Unknown command. Type 'HELP' to see the list of commands.")
