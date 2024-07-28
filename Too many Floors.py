# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    x=(x-1)//10
    y=(y-1)//10
    print(abs(x-y))