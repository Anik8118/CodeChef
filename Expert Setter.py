for _ in range(int(input())):
    x,y=map(int,input().split())
    if (y*100)//x<50:
        print("NO")
    else:
        print("YES")