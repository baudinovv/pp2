start = int(input())
N = int(input())
def createGenerator(start,N):
    for i in range(start,N):
        yield i**2
        

squares = list(createGenerator(start,N))

print(', '.join(map(str, squares )))