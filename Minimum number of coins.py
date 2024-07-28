for _ in range(int(input())):
    x=int(input())
    if x%5!=0:
        print(-1)
    else:
        if x%5==0 and x%10==0:
            print(x//10)
        elif x%5==0:
            print((x//10)+1)