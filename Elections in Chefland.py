for _ in range(int(input())):
    x,y=map(int,input().split())
    lst=list(map(int,input().split()))
    c=0
    for i in range(x):
        if lst[i]>=y:
            c+=1
    print(c)        
    