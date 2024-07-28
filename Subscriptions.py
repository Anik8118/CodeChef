for _ in range(int(input())):
    a,b=map(int,input().split())
    if a%6==0:
        print((a//6)*b)
    else:
        print(((a//6)+1)*b)
        
    