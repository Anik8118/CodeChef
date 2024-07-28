for _ in range(int(input())):
    x,y=map(int,input().split())
    if 21-(x+y)>=1 and 21-(x+y)<=10:
        print(21-(x+y))
    else:
        print(-1)