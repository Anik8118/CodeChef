# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    if w/y<x/z:
        print("Chef")
    elif w/y>x/z:
        print("Chefina")
    else:
        print("Both")