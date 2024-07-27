t=int(input())
while t>0:
    a,b=map(int,input().split())
    c=(a*10)//100
    print((a+c)-(a-b))
    t-=1
    