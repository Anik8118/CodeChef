t=int(input())
while t>0:
    a,b=map(int,input().split())
    if a*5>=b:
        print("YES")
    else:
        print("NO")
    t-=1
    