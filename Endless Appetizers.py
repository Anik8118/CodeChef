# cook your dish here
import math
for _ in range(int(input())):
    x,y,r=map(int,input().split())
    print(math.ceil(((r/30)+x)/y))