def has33(list):
    cnt = 0
    for i in list:
        if(i == 3): cnt = cnt + 1
    if(cnt >= 2):
        return True
    return False
print(has33([1, 3, 3, 1 , 3]))