# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x>=y:
        print("PIZZA")
    elif x<y and x>=z:
        print("BURGER")
    else:
        print("NOTHING")