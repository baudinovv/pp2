str = input()
str2 = "".join(reversed(str))
if str == str2:
    print("YES")
else:
    print("NO")