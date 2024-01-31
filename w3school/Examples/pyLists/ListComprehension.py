fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Syntax
# newlist = [<expression> for <item> in <iterable> if <condition> == True]

newlist = [x for x in fruits if x != "apple"] # ['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits] # ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5] # [0, 1, 2, 3, 4]

newlist = [x.upper() for x in fruits] # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits] # ['hello', 'hello', 'hello', 'hello', 'hello']

newlist = [x if x != "banana" else "orange" for x in fruits] # ['apple', 'orange', 'cherry', 'kiwi', 'mango']



