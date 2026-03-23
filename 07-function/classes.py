# class is defining and design an entity from scrach

class User: # class has the initial letter Capital letter, has to be an signle entity. 
    # must have an init method to initialise the class. 
    #self is a self pointer of an instance inside of the class.
    def __init__(self, first_name, last_name, city, age):
        self.f_name = first_name # what after the self. is the proparety of the class
        self.l_name = last_name
        self.city = city
        self.age = age

user1 = User("John", "Wick", "Paris", 37)

def print_user_info(user):
    print(f"First name: {user.f_name}")
    print(f"Last name: {user.l_name}")
    print(f"City: {user.city}")

