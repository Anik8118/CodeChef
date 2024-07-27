for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        if b+c<a:
            print("YES")
        else:
            print("NO")
    elif b>a and b>c:
        if a+c<b:
            print("YES")
        else:
            print("NO")
    elif c>a and c>b:
        if a+b<c:
            print("YES")
        else:
            print("NO") 
    else:
        print("NO")
    