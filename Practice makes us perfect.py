a,b,c,d=map(int,input().split())
i=0
for x in [a,b,c,d]:
    if x>=10:
        i+=1
print(i)    