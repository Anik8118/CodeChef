t=int(input())
while t>0:
    a,b=map(int,input().split())
    c=a-b
    if c<=b:
        print("YES")
    else:
        print("NO")
    t-=1  
    