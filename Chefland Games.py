for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    if (w,x,y,z) in [
        (1,1,1,1),(1,1,1,0),(1,1,0,1),(1,0,1,1),(0,1,1,1),(1,1,0,0),(1,0,0,1),(0,0,1,1),
        (1,0,1,0),(0,1,1,0),(0,1,0,1),(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0),
    ]:
        print("OUT")
    else:
        print("IN")