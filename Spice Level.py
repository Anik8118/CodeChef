t=int(input())
while t>0:
    a=int(input())
    if a<4:
        print("MILD")
    elif a>=4 and a<7:
        print("MEDIUM")
    elif a>=7:
        print("HOT")
    t-=1 
    