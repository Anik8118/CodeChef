t=int(input())
while t>0:
    a,b=map(int,input().split())
    if 2*a>b:
        print("FIRST")
    elif 2*a<b:
        print("SECOND")
    else:
        print("ANY")
    t-=1