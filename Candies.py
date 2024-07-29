# cook your dish here
for _ in range(int(input())):
    x=int(input())
    lst=list(map(int,input().split()))
    print("YES" if max(lst.count(a) for a in lst)<=2 else "NO")