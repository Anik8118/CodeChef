# cook your dish here
import math
for _ in range(int(input())):
    a,b,k=map(int,input().split())
    print(math.ceil((abs(a-b))/k))