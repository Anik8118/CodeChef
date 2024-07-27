t=int(input())
for x in range(t):
    a,b,c=map(int,input().split())
    if a+b==c:
        print("YES")
    else:
        print("NO")
    