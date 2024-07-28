for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print("Qualify" if y+2*z>=x else "NotQualify")