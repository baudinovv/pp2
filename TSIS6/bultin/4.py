import time
import math

delay = int(input())
num = int(input())

if(delay >= 1000):
    delay = delay / 1000

time.sleep(delay)

print(math.sqrt(num))