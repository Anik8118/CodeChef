for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>y:
        print("CAR")
    elif x<y:
        print("BIKE")
    else:
        print("SAME")