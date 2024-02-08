def spy_game(nums):
    cnt1 = 0
    flag = True
    for i in nums:
        if(i == 0): cnt1 = cnt1 + 1
        if(cnt1 >= 2):  flag = False
        if(i == 7 and cnt1 >= 2):  return True

    return False


print(spy_game([7,0,4,2,0,5]))