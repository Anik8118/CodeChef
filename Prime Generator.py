def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
                
                
def Prime(n,m):
    for i in range(n,m+1):
        if isPrime(i):
            print(i)
    print(" ")        
        
        
for _ in range(int(input())):
    x,y=map(int,input().split())
    Prime(x,y)
    

    
 