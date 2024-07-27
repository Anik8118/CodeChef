t=int(input())
while t>0:
    a,b=map(int,input().split())
    print(min(3*a,2*b))
    t-=1
    