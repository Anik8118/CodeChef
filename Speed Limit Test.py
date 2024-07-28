# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    if w/x<y/z:
        print("Bob")
    elif w/x>y/z:
        print("Alice")
    else:
        print("Equal")