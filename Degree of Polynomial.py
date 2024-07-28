# cook your dish here
for _ in range(int(input())):
    x=int(input())
    lst=list(map(int,input().split()))
    c=0
    for i in range(x-1,-1,-1):
        if lst[i]!=0:
            c=i
            break
    print(c)    