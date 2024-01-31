thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # by index
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() # last item 
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] # first item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist # delete entire list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # list now empty

