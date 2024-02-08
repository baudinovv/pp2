def palin(str):
    result = str[::-1]
    if(str == result): return True
    return False
print(palin("ada"))