
import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    temp=(x*y)/4
    print(math.ceil(temp))