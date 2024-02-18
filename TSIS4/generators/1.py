N = int(input())

def createGenerator(N):
    for i in range(N):
        yield i**2

mygen = createGenerator(N + 1)

for i in mygen:
    print(i)