# cook your dish here
for _ in range(int(input())):
    n,x,c=map(int,input().split())
    lst=list(map(int,input().split()))
    print(sum(max(i,x-c) for i in lst))

 