t=int(input())
while t>0:
    a,b,c=map(int,input().split())
    if b*c>=a:
        print("YES")
    else:
        print("NO")
    t-=1
    