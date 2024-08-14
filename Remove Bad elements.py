for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    frequency={}
    for num in lst:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1
    max_frequency=max(frequency.values())
    min_removal=n-max_frequency
    print(min_removal)
