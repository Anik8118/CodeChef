for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a*10>=b:
        print(b*c)
    elif a*10<b:
        print(c*a*10)
    