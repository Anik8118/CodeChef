for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if c/(a*b)*100<=50:
        print("NO")
    else:
        print("YES")s    