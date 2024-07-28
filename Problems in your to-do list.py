lst=[]
p=int(input())
while p>0:
    c = 0
    t = int(input())
    lst=list(map(int,input().split()))
    for i in range(t):
        if lst[i]>=1000:
            c+=1
    p-=1        
    print(c)