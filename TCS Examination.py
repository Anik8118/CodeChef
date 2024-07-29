# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    if (a+b+c)>(x+y+z):
        print("DRAGON")
    elif (a+b+c)<(x+y+z):
        print("SLOTH")
    elif (a+b+c)==(x+y+z):
        if a>x:
            print("DRAGON")
        elif a<x:
            print("SLOTH")
        elif a==x:
            if b>y:
                print("DRAGON")
            elif b<y:
                print("SLOTH")
            elif b==y:
                if c>z:
                    print("DRAGON")
                elif  c<z:
                    print("SLOTH")
                elif c==z:
                    print("TIE")