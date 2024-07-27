for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a+c*d>b:
        print("overFlow")
    elif a+c*d==b:
        print("filled")
    elif a+c*d<b:
        print("Unfilled")
    