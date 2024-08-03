# cook your dish here
for _ in range(int(input())):
    y,p=map(int,input().split())
    c=0
    if p%2==0:
        c+=p//2
    else:
        c+=(p+1)//2
    if y%2==0:
        c*=y//2
    else:
        c*=(y+1)//2
    print(int(c))
    
