"""
Practical - 5
Name: Mohit Marvania
ID: 20CS033
CE259 PIP

Que: You are given a string and your task is to swap cases.
     In other words, convert all lowercase letters to uppercase
     letters and vice versa.
"""

# Taking the input as string from the user.
stringToenter = input()

# creating an array to store the character from the string.
final = []

# Checking the string char by char and
# converting vise versa to it and appending in the list.
for item in stringToenter:
    if item.islower():
        final.append(item.upper())
    elif item.isupper():
        final.append(item.lower())
    else:
        final.append(item)

# Printing the result with the help of join function on final list.
print(''.join(final))

# deleting final to explicitly free up the space.
del final

