import math
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print(min(x,math.floor(z/y)))