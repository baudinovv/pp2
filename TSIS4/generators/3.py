N = int(input())

def createGenerator(N):
    for i in range(N):
        if(i % 3 != 0 and i % 4 != 0):
            continue
        yield i

mygen = createGenerator(N )

mygenlist = list(mygen)

print(', '.join(map(str, mygenlist)))