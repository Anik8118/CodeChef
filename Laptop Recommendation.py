# cook your dish here
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    v = list(map(int,input().split()))
    m = Counter()
    for i in v:
        m[i] += 1

    count = 0
    ans = 1
    for i in m:
        if m[i]>=count:
            count = m[i]
            ans = i
            
    confusion = 0
    for i in m:
        if m[i]==count:
            confusion+=1

    if confusion > 1:
        print("confused")
    else:
        print(ans)