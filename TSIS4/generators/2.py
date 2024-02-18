N = int(input())

def createGenerator(N):
    for i in range(N):
        if(i % 2 != 0):
            continue
        yield i

mygen = createGenerator(N )

mygenlist = list(mygen)

print(', '.join(map(str, mygenlist)))