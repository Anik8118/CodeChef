# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if 3*y-(x-y)>=z:
        print("PASS")
    else:
        print("FAIL")