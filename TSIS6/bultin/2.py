str = input()
def upper(str):
    return str.isupper()
def lower(str):
    return str.islower()
uppstr = sum(map(upper, str))
lowstr = sum(map(lower, str))
print(f"Upper case letters: {uppstr} \nLower case letters: {lowstr}")