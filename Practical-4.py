"""
Practical - 4
Name: Mohit Marvania
ID: 20CS033
CE259 PIP

Que: Find runner-up from given list
"""
import sys

# Taking the total number of runs to be entered by the user.
T = int(input())

# Creating the array of the runs entered by the user.
runs = [int(i) for i in input().split(' ')]

# Checking if the runs entered by the user is equal to the total number of runs.
if len(runs) != T:
    sys.exit()

# storing the runs as list by setting and sorting it.
sorted_runs = list(set(sorted(runs)))

# printing the result which is the runner up from the list.
print(sorted_runs[-2])
