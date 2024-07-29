# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    if lst.count(1)%2!=0:
        print("NO")
    else:
        print("YES")