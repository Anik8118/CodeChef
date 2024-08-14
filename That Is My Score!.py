# cook your dish here
for _ in range(int(input())):
    a=int(input())
    lst=[0]*12
    for i in range(a):
        n,m=map(int,input().split())
        lst[n]=max(lst[n],m)
    c=0
    for i in range(9):
        c+=lst[i]
    print(c)