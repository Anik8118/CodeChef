# cook your dish here
for _ in range(int(input())):
    x=int(input())
    lst=list(map(int,input().split()))
    c=0
    for i in lst:
        if i>=10 and i<=60:
            c+=1
    print(c) 