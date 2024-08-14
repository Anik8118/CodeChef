# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    temp=sorted(s)
    for i in range(n-1):
        if temp[i]==temp[i+1]:
            print(n-2)
            break
    else:
        print(-1)