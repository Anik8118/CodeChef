# cook your dish here
for _ in range(int(input())):
    x=int(input())
    lst=list(input().split())
    s=0
    t=0
    for i in lst:
        if i=="START38":
            s+=1
        else:
            t+=1 
    print(s ,t)        