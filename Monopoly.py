# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    a=max(w,x,y,z)
    if a==w:
        if x+y+z<w:
            print("YES")
        else:
            print("NO")
    elif a==x:
        if w+y+z<x:
            print("YES")
        else:
            print("NO")
    elif a==y:
        if w+x+z<y:
            print("YES")
        else:
            print("NO")
    elif a==z:
        if w+x+y<z:
            print("YES")
        else:
            print("NO")
        

        