t=int(input())
while t>0:
    a,b=map(int,input().split())
    if a>b:
        print("SECOND")
    elif a<b:
        print("FIRST")
    elif a==b:
        print("ANY")
    t-=1
    