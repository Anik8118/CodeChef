t=int(input())
while t>0:
    x=int(input())
    c=1
    if x==0 or x==1:
        print(1)
    else:
        for i in range(2,x+1,1):
            c*=i
        print(c)   
    t-=1