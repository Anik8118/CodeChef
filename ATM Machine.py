# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    lst=list(map(int,input().split()))
    s=''
    for i in lst:
        if i<=y:
            y-=i 
            s+='1'
        else:
            s+='0'
    print(s)        
        