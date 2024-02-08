def toUnique(list):
    result = []
    for i in list:
        cnt = 0
        for j in list:
            if(i == j): cnt = cnt + 1
        if(cnt >= 2): continue
        result.append(i)
    print(result)

toUnique([1, 1, 1 , 2 , 2 , 3 ,3 , 4 , 9 , 2 , 1])
            