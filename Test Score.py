for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print("YES" if z%y==0 else "NO")