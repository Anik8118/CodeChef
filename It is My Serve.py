# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    if ((x+y)//2)%2==0:
        print("Alice")
    else:
        print("Bob")