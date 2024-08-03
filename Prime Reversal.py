# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s1=input()
    s2=input()
    if s1==s2:
        print("YES")
    else:
        x,y,a,b=s1.count('0'),s1.count('1'),s2.count('0'),s2.count('1')
        if x==a:
            print("YES")
        else:
            print("NO")
    