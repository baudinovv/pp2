import math

def filter_prime(list):
    def isPrime(num):
        cnt = 0
        for j in range(1 , num + 1):
            if(num % j == 0):
                cnt = cnt + 1
        if(math.floor(cnt) == 1):
            return True
        else:
            return False
    for i in list:
        if(isPrime(i) == False):
            list.remove(i)
    return list

print(filter_prime([1, 2 , 3, 4 ,5 ,6 ,7, 8,9,10,11,12,13,14,15,16,17]))
            
                
        