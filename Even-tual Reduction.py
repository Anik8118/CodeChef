# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    if len(s)%2!=0:
        print("NO")
    else:
        c=0
        for i in s:
            if s.count(i)%2==0:
                c+=1 
            else:
                break
        if c==len(s):
            print("YES")
        else:
            print("NO")