"""
Practical - 6
Name: Mohit Marvania
ID: 20CS033
CE259 PIP

Que: You are given n words. Some words may repeat.
     For each word, output its number of occurrences.
     The output order should correspond with the input
     order of appearance of the word.
"""

from collections import Counter

words = []
for i in range(int(input())):
    words.append(input())

c = Counter(words)
print(len(c))
for i in c:
    print(c.get(i), end='\n')
print()
