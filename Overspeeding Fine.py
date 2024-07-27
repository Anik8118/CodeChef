t=int(input())
while t>0:
    a=int(input())
    if a<=70:
        print(0)
    elif a>70 and a<=100:
        print(500)
    elif a>100:
        print(2000)
    t-=1 
    