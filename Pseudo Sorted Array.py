# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    for i in range(n-1):
        if lst[i]>lst[i+1]:
            temp=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=temp
            break
    if lst==sorted(lst):
        print("YES")
    else:
        print("NO")