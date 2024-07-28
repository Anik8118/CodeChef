t=int(input())
while t>0:
    x, y = map(int, input().split())
    print("YES" if y%x==0 else "NO")
    t-=1