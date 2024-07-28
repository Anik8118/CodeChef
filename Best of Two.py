# cook your dish here
for _ in range(int(input())):
    a,b,c,x,y,z=map(int,input().split())
    if a+b+c-min(a,b,c)>x+y+z-min(x,y,z):
        print("Alice")
    elif a+b+c-min(a,b,c)<x+y+z-min(x,y,z):
        print("Bob")
    else:
        print("Tie")