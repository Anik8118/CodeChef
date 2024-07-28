# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print("YES" if abs(x-y)<=z else "NO")