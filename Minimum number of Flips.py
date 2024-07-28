for _ in range(int(input())):
    x=int(input())
    lst=list(map(int,input().split()))
    if x%2!=0:
        print(-1)
    else:
        t1=lst.count(1)
        t2=lst.count(-1)
        print(abs(t1-t2)//2)
        
        
        
        
