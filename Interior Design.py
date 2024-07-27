t=int(input())
while t>0:
    a,b,c,d=map(int,input().split())
    e=a+b
    f=c+d
    if e>f:
        print(f)
    else:
        print(e)
    t-=1
    