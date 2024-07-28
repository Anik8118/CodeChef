for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print(y*(x//2) +z*(x-x//2))