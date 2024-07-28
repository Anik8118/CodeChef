for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if max(x,z)<=y:
        print("YES")
    else:
        print("NO")
