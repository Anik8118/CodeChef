# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(n):
        if lst1[i]>lst2[i]:
            c1=1 
        if lst1[i]>lst2[n-1-i]:
           c2=1 
    if c1==0 and c2==0:
        print("both")
    elif c1==1 and c2==1:
        print("none")
    elif c1==1:
        print("back")
    else:
        print("front")
