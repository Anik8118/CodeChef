for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    result=z-(w-(x+y))
    if result<=0:
        print(0)
    elif result<=max(x,y):
        print(1)
    else:
        print(2)