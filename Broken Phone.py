for _ in range(int(input())):
    x,y=map(int,input().split())
    if y>x:
        print("REPAIR")
    elif x>y:
        print("NEW PHONE")
    else:
        print("ANY")
    