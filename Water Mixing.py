for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    if a-y<=b and a+x>=b:
        print("YES")
    else:
        print("NO")