import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    if y>x:
        print(0)
    else:
        print(math.floor(x/(2*y)))