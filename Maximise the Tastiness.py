lst=[]
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    print(max(w,x)+max(y,z))