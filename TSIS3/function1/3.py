import math

def solve(numheads, numlegs):
    rabbits = math.fabs((numheads * 2) - numlegs)
    return math.floor(rabbits/2), math.floor(numheads - rabbits/2);   

print(solve(34 , 94))
