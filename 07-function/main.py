# function all have a name and followed by ()
#define a function starts with def function_name():

import random #can also import an function for using. 

random.randint(1, 5)

def foo():
    print("Hello World")

# define a function with inputs
def greet(name):
    print(f"Hello {name}")

def sum(a, b):
    result = a + b
    return result #return is not print to the screen. 
sum1 = sum(2, 5)
print(sum1)

def display_number(n, even=True):
    for number in range(n):
        if even:
            if number % 2 == 0:
                print(number)
        else: 
            print(number)

display_number(15, True )

# functions can have multiple returns, as the return ends the function. 
def get_fisrt_smallets_number(list_numbers, even=True):
    list_numbers = sorted(list_numbers) # sorted() is a fucntion that orders the number inside a list. 
    for numbers in list_numbers:
        if even:
            if numbers % 2 == 0: 
                return numbers
        else: 
            if numbers % 2 != 0: 
                return numbers
            
list_n = [0, 35, 6, 2, 44]
get_fisrt_smallets_number(list_n, False)

def f_multiple_args(*args): #with * it can receive multiple arguments inputs for the function
    return args

v1 = f_multiple_args(1, 5, 6)
v2 = f_multiple_args(35, 6, 200, 53, 6)
print(v1)