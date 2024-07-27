t=int(input())
while t>0:
    a,b=map(int,input().split())
    if 2*b>a:
        print("NO")
    else:
        print("YES")
    t-=1