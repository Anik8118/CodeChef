# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if (x>y and x<z) or (x>z and x<y):
        print(x)
    elif (y>x and y<z) or (y>z and y<x):
        print(y)
    elif (z>x and z<y) or (z>y and z<x):
        print(z)
