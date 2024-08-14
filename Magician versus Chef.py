# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    temp=y
    while z>0:
        a,b=map(int,input().split())
        if temp==a:
            temp=b 
        elif temp==b:
            temp=a 
        z-=1 
    print(temp)    