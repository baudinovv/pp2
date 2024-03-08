num = [int(char) for char in input().split()]
print(eval('*'.join(str(item) for item in num)))