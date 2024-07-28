for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x<y*z:
        print(1)
    elif x%(y*z)==0:
        print(x//(y*z))
    elif x//(y*z)>0:
        print(x//(y*z)+1)
    