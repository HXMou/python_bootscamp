# class is defining and design an entity from scrach

class User: # class has the initial letter Capital letter, has to be an signle entity. 
    # must have an init method to initialise the class. 
    #self is a self pointer of an instance inside of the class.
    def __init__(self, first_name, last_name, city, age):
        self.f_name = first_name # what after the self. is the proparety of the class
        self.l_name = last_name
        self.city = city
        self.age = age

    #methods of class
    # Always must use self as the first peramiter 
    def print_detail(self):
        print(f"First name: {self.f_name}")
        print(f"Last name: {self.l_name}")
        print(f"City: {self.city}")

    def print_hello(self):
        print(f"Hello {self.f_name}")

class ProductPiece:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getPrice(self, quantity):
        total_price = quantity*self.price

class Dog:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f"{self.name} is barking!")

torvi = Dog("Torvi")

torvi.make_noise()