t=int(input())
for x in range(t):
    a,b=map(int,input().split())
    if b>=a:
        print("YES")
    else:
        print("NO")
    