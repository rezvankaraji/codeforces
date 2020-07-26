arge = input().split(" ")
n = int(arge[0])
t = int(arge[1])

read_queue = input()

queue = []
new_queue = []

for x in read_queue:
    queue.append(x)
    new_queue.append(x)

while t > 0:
    for i in range(n):
        queue[i] = new_queue[i]
    for i in range(1, n):
        if queue[i - 1] == 'B' and queue[i] == 'G':
            new_queue[i - 1] = 'G'
            new_queue[i] = 'B'
    t = t - 1


for x in new_queue:
    print(x, end = '')


