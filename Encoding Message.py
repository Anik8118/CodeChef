for _ in range(int(input())):
    n=int(input())
    s=input()
    temp=str()
    temp1=str()
    i=0
    if n%2==0:
        while i<n:
            temp=temp+s[i+1]+s[i]
            i+=2
    else:
        while i<(n-1):
            temp=temp+s[i+1]+s[i]
            i+=2
        temp=temp+s[n-1]
    j=0    
    while j<n:
        temp1=temp1+chr(97+122-ord(temp[j]))
        j+=1 
    print(temp1)