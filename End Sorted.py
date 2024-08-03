for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    x=lst.index(1)
    y=n-1-lst.index(n)
    if lst.index(1)<lst.index(n):
        print(x+y)
    else:
        print(x+y-1)