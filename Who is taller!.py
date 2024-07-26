t=int(input())
for x in range(t):
    a,b=map(int,input().split())
    if a>b:
        print("A")
    elif b>a:
        print("B")
    