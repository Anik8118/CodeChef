T = int(input())
while T>0:
    N,K = map(int, input().split())
    L = []
    count = 0
    L[0:N-1] = map(int, input().split())
    for i in range(N):
        L[i] = L[i]+K
        if L[i]%7==0:
            count+=1
    print(count)
    T-=1 