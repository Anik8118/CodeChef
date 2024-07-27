t=int(input())
while t>0:
    a=int(input())
    if a<3:
        print("LIGHT")
    elif a>=3 and a<7:
        print("MODERATE")
    elif a>=7:
        print("HEAVY")
    t-=1 
    