# cook your dish here
import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    ex=math.ceil(y/100)
    print(0 if ex<x else ex-x)
    