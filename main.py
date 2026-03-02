#list

list1 = [1, 2, 44, 5]
list2 = []

print(list1, type(list1))

#python can use "" and '' mix used for string
list_of_string = ["aaa", 'bbb'] 
print(list_of_string, type(list_of_string))

list_of_booleans = [True, True, False]
print(list_of_booleans, type(list_of_booleans))

s_int = 231
s_float = 3.1415
s_string = "hey"
s_bool = True

list_of_mix = [1, 3.1415, s_string, s_bool, [1,2,3], list_of_string]

print("-- Try with the loop.--")
for i in list_of_mix:
    if type(i) == list:
        for inner_item in i:
            print("\t", inner_item)
    else:
        print(i)

# to display only one element need to use indexes to local in the list. 
print(f"first element 0: {list_of_string[0]}")
print(f"the last element: {list_of_string[len(list_of_string) - 1]}")

# -1 for the last element's index always works. 
# When the list only have one element, list[0] = list[-1]
print(f"Simpler way to display the last element: {list_of_string[-1]}")
print(f"The second last element of the list: {list_of_string[-2]}")

index = 0
while index < len(list1): # can not set index <= length as the index starts from 0. 
    print(list1[index])
    index += 1

for index in range(len(list1)):
    print(list1[index])
    index += 1

my_list = [100, 200, 300]
print(my_list)

my_list.append(400) # adding an element to the end of the list
my_list.insert(1, "Mou") # specify at where to insert the new element

print(my_list)

# Dictionaries
dict1 = {} #be careful!
dict2 = dict()

print(dict1, type(dict1))

dict3 = {
    "key1": 100,
    "key2": "some value",
    "key3": 5.25
    } #keys in dict are always a string but values can be any type 

print(dict3, type(dict3))
print("length:", len(dict3))

print(dict3["key2"]) #in dict there is no oder but needs to use the name of the key for print

for key in dict3:
    print(key, dict3[key])

for key in dict3.keys():
    print(key, dict3[key])
    
for value in dict3.values():
    print(value)

for key, value in dict3.items():
    print(f"key: {key}, value: {value}")

# add element to a dictionary
my_dict = {
    "first_name": "Iris",
    "last_name": "Mou",
    "age": 26
}

my_dict["city"] = "Cork"

print(my_dict)