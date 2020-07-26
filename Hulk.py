n = int(input())

for i in range(n):
    if i == 0 :
        print("I hate", end = ' ')
    elif i % 2 == 0:
        print("that I hate", end = ' ')
    elif i % 2 == 1:
        print("that I love", end = ' ')

    if i == n - 1:
        print("it")

    

