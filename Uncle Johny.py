# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    k=int(input())
    #temp1=lst[k-1]
    temp2=sorted(lst)
    for i in range(n):
        if temp2[i]==lst[k-1]:
            print(i+1)
            break