for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    if w*x<=y*z:
        print("Yes")
    else:
        print("No")