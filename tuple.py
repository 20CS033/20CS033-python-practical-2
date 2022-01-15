"""
Program for Practical - 2
Name : Mohit Marvania
ID : 20CS033

Tuple

a. Write a Python program to create a tuple with different data types.
b. Write a Python program to create a tuple with numbers and print one item.
c. Write a Python program to add an item in a tuple.
d. Write a Python program to convert a tuple to a string.
e. Write a Python program to find the length of a tuple.

"""

# A) Write a Python program to create a tuple with different data types.
new_tuple = (1, "One", 2.13)
print(new_tuple)

# B) Write a Python program to create a tuple with numbers and print one item.
tuples = (1, 4, "79")
print(tuples[2])

# C) Write a Python program to add an item in a tuple.
tup = (123, 456, 789)
print(tup)
# we cannot add item in tup.

# D) Write a Python program to convert a tuple to a string.
tupl = ("1", "2", "3", "4", "5")
str = ''
for item in tupl:
    str = str + item
print(str)

# E) Write a Python program to find the length of a tuple.
new_tuple = ("One", "Two", "Three", "Four", "Five", "Six")
count = 0
for item in new_tuple:
    count += 1
print(count)

