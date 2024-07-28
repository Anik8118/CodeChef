# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    temp=max((x+y),(y+z),(z+x))
    print(temp)