thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # if element doesn't exist, it will NOT return error

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) # removed random item

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # empty set

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)