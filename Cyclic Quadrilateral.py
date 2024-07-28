# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    if w+y==180 and x+z==180:
        print("YES")
    else:
        print("NO")