t=int(input())
while t>0:
    a,b=map(int,input().split())
    if a*100>=b*10:
        print("Cloth")
    else:
        print("Disposable")
    t-=1 
    