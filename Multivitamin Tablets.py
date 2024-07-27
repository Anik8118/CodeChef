t=int(input())
while t>0:
    a,b=map(int,input().split())
    if b-a*3>=0:
        print("YES")
    else:
        print("NO")
    t-=1
    