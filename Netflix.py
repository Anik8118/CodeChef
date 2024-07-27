for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a+b>=d or b+c>=d or c+a>=d:
        print("YES")
    else:
        print("NO")
    