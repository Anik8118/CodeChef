t=int(input())
for x in range(t):
    a,b=map(int,input().split())
    if a>b:
        print("LOSS")
    elif a==b:
        print("NEUTRAL")
    elif a<b:
        print("PROFIT")
    