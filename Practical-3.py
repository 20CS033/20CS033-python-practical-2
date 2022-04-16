"""
Practical - 3
Name: Mohit Marvania
ID: 20CS033
CE259 PIP

Que: Find Captain Room Number
"""

# Taking the number for matching the rooms.
K = int(input())

# Creating and array of total number of rooms entered by the user.
rooms = [int(i) for i in input().split(' ')]

# storing the sorted and set array of rooms in the new array.
# and comparing each value of sorted_array with each value of rooms.
sorted_array = list(set(sorted(rooms)))
captions_room = None

# A loop which takes value from sorted_array and
# then compares with each value from rooms.
for item in sorted_array:
    yes = 0
    no = 0
    for i in rooms:
        if item == i:
            yes += 1
        else:
            no += 1
    if yes == K:
        continue
    else:
        captions_room = item

# Prints the result which is the captions room no.
print(captions_room)