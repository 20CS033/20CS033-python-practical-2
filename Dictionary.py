"""
Program for Practical - 2
Name : Mohit Marvania
ID : 20CS033

Dictionary:

a. Write a Python script to check whether a given key already exists in a dictionary.
b. Write a Python script to merge two Python dictionaries.
c. Write a Python program to sum all the items in a dictionary.
d. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
e. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""

# Dictionary

# A) Write a Python script to check whether a given key already exists in a dictionary.
dict1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'four', 5: 'Five'}
new_key = int(input("Enter the key"))

if new_key in dict1:
    print("True")
else:
    print("False")

# B) Write a Python script to merge two Python dictionaries.
dicti1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
dicti2 = {'One': 123, 'Two': 234, 'Three': 345, 'Four': 456}
print(dicti1)
dicti1.update(dicti2)
print(dicti1)

# C) Write a Python program to sum all the items in a dictionary.
dict_1 = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6}
for item in dict_1.items():
    item += item
    print(item)

# D) Write a Python script to add a key to a dictionary.
sample_dict = {0: 10, 1: 20}
print("Initial dict - ", sample_dict)
sample_dict[2] = 30
print("Updated dict - ", sample_dict)

# E) Write a Python script to concatenate following dictionaries to create a new one.
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

