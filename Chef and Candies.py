import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    need=x-y
    if need<=0:
        print(0)
    else:
        print(math.ceil(need/4))