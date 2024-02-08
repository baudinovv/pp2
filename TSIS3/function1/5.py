from itertools import permutations

def perm(str):
    return list(permutations(str))

for i in perm("hello"):
    print(i)