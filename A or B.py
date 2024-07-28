# cook your dish here

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a1=500-x*2
    b1=1000-(x+y)*4
    b2=1000-y*4
    a2=500-(y+x)*2
    if a1+b1>a2+b2:
        print(a1+b1)
    else:
        print(a2+b2)