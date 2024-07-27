for _ in range(int(input())):
    a,b,c=map(int,input().split())
    maximum=max(a,b,c)
    if a>b and a>c:
        if c+b<a:
            print("YES")
        else:
             print("NO")
    elif b>a and b>c:
        if c+a<b:
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
    