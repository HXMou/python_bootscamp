def load_books():
    books = dict()
    with open("books.txt", "r") as f:
        for line in f: 
            title, quantity = line.strip().split(",") #telling python to split the code when meet , marks
            books[title] = int(quantity)
    return books

def update_books(books):
    with open("books.txt", "w") as f:
        for title, quantity in books.items():
            f.write(f"{title}, {quantity}")

def display_help():
    print("""List of available commands:
              """)
    
def display_history(history):
    print("Commands history: \n")
    for order, item in history:
        print(f"{order+1}. {item}")

def dispaly_volume_count(books):
    print("Total number of books: ")
    print(sum(books.values()))

def unique_book_title(books):
    print("Check the unique number of all titles:\n")
    unique_count = len(books)
    print(unique_count)

def availability_check(books):
    print("Check if the book is available.\n")
    title = input("Enter book title: ")
    if title in books:
        print(f"{books[title]} of {title} is available.")
    else:
        print(f"{title} is not available. ")

def list_all_books(books):
    print("Lists of books:\n")
    if books: #check firstly if book exists 
        for title, quatity in books.items():
            print(f"- \"{title}\":{quatity} pcs.")

def borrow_books(books):
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
        
        update_books(books)
        return books

def add_books(books):
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

        update_books(books)
        return books

