for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    print(max(abs(w-y),abs(x-z)))