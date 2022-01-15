"""
Program for Practical - 2
Name : Mohit Marvania
ID : 20CS033

Set

a. Write a Python program to add member(s) in a set and clear a set
b. Write a Python program to remove an item from a set if it is present in the set.
c. Write a Python program to create an intersection, Union, difference of sets.
d. Write a Python program to find maximum and the minimum value in a set.
e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

"""

# A) Write a Python program to add member(s) in a set and clear a set
my_set = {1.2, 2.3, 3.4}
print("Initial set = ", my_set)
my_set.add(4.5)
print("Updated set = ", my_set)
my_set.clear()
print(my_set)

# B) Write a Python program to remove an item from a set if it is present in the set.
new_set = {"Mango", "Apple", "Orange", "Strawberry", "Watermelon"}
print("New set = ", new_set)
new_set.remove("Watermelon")
print("Updated set = ", new_set)

# C) Write a Python program to create an intersection, Union, difference of sets.
set_1 = {1, 2, 3, 4, 5, 9, 10}
set_2 = {6, 7, 8, 9, 10}
print("Intersection of set1 and set2 = ", set_1.intersection(set_2))
print("Union of set1 and set2 = ", set_1.union(set_2))
print("Difference of set1 and set2 = ", set_1.difference(set_2))

# D) Write a Python program to find maximum and the minimum value in a set.
set_initial = {124, 12412, 6436, 6892, 2852}
print(max(set_initial))
print(min(set_initial))

# E) Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
new_list = [1, 3, 25, 45, 132, 25, 92, 245, 25, 92, 25, 9234]
new_tuple = (3, 12, 41, 421, 12, 943, 12, 4929, 593, 94, 12)
new_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Two", 6: "Six", 7: "Two"}

# For list
dicti = {}
for item in new_list:
    dicti[new_list.count(item)] = item

print(dicti.get(max(dicti.keys())))

# For tuple
dicti2 = {}
for item in new_tuple:
    dicti2[new_tuple.count(item)] = item

print(dicti2.get(max(dicti2.keys())))
