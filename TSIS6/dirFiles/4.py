import os
str = 0
with open('ex2.txt', 'r') as line:
    for x in line: str += 1
print(str)