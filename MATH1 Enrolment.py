t=int(input())
while t>0:
    a,b=map(int,input().split())
    if b>=a:
        print(b-a)
    else:
        print(0)
    t-=1   
    