# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    lst3=[]
    for i in range(len(lst1)):
        temp=lst1[i]*20-lst2[i]*10
        if temp>0:
            lst3.append(temp)
        else:
            lst3.append(0)
    print(max(lst3))        