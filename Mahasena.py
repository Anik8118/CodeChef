even=0
odd=0
t=int(input())
li=list(map(int,input().split()))
for i in li:
    if i%2==0:
        even+=1
    elif i%2!=0:
        odd+=1
if even>odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")