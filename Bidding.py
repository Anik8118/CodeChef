t=int(input())
while t>0:
    a,b,c=map(int,input().split())
    maximum=max(a,b,c)
    if maximum==a:
        print("Alice")
    elif maximum==b:
        print("Bob")
    else:
        print("Charlie")
    t-=1 
    