
N = int(input())
def createGenerator(N):
    for i in range(-N, 0):
        yield -i
        

squares = list(createGenerator(N))

print(', '.join(map(str, squares )))