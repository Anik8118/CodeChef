
    t=int(input())
for x in range(t):
    a,b=map(int,input().split())
    if b>a:
        print(0)
    else:
        print(a-b)