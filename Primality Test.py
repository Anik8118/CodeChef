# cook your dish here
for _ in range(int(input())):
    x=int(input())
    c=0
    for i in range(2,(x+1),1):
        if x%i==0:
            c+=1 
            
    if c==1:
        print("yes")
    else:
        print("no")
        
        
      