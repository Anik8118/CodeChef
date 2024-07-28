# cook your dish here
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    if w!=y and w!=z and x!=y and x!=z:
        print(2)
    elif (y==w or y==x) and (z==w or z==x):
        print(0)
    else:
        print(1)