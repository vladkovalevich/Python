import math
orders = int(input())
for i in range(orders):
    
    z1 = input().split(' ')

    L = int(z1[0])
    W = int(z1[1])
    H = int(z1[2])

    if(L > 1000 and W > 1000 and H > 1000):
        print("Error")
        continue
    s = 2 * (W + L) * H
    s = s / 16
    print(math.ceil(s))
