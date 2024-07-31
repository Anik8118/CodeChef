# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    lst=list(map(int,input().split()))
    c=0
    p=0
    for i in range(x):
        if lst[i]+c>=y:
            c=lst[i]+c-y
        else:
            p=i+1
            break
    if p!=0:
        print("NO ",p)
    else:
        print("YES")