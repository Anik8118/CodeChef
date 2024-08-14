# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    c=0
    for i in range(n-1):
        c+=(abs(lst[i]-lst[i+1])-1)
    print(c)    