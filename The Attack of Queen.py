# cook your dish here
for i in range(int(input())):
    n,X,Y=map(int,input().split())
    print((n*2-2)+min(X-1,n-Y)+min(X-1,Y-1)+min(n-X,Y-1)+min(n-X,n-Y))