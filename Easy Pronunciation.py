# cook your dish here
for _ in range(int(input())):
    x=int(input())
    lst=input()
    c=0
    temp=0
    for i in range(x):
        if lst[i]!='a' and lst[i]!='e' and lst[i]!='o' and lst[i]!='u' and lst[i]!='i':
            c+=1
        else:
            if c>=4:
                temp=1 
                break
            c=0
    if c>=4:
        temp=1
    if temp==1:
        print("NO")
    else:
        print("YES")