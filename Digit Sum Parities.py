# cook your dish here
def digitsum(n):
    dsum = 0
    while n>0:
        dsum+=(n%10)
        n = int(n/10)
    return dsum
T = int(input())
while T>0:
    N = int(input())
    X = N+1
    if digitsum(N)%2==0:
        while X>N:
            if digitsum(X)%2==0:
                X+=1
            else:
                print(X)
                break
    else:
        while X>N:
            if digitsum(X)%2==1:
                X+=1
            else:
                print(X)
                break
    T-=1