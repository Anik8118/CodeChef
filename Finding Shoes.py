for _ in range(int(input())):
    x,y=map(int,input().split())
    print(2*x-y if x>y else x) 