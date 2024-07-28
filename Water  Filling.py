for _  in range(int(input())):
    x,y,z=map(int,input().split())
    if (x,y,z)==(0,0,0) or (x,y,z)==(0,1,0) or (x,y,z)==(1,0,0) or (x,y,z)==(0,0,1):
        print("Water filling time")
    else:
        print("Not now")