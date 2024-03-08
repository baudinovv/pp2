import os
path = os.getcwd()
def check(Anotherpath):
    if os.access(Anotherpath, os.F_OK):
        print(os.listdir(path))
    else:
        print("Given path doesn't exist")
check(path) 