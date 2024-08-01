# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    z,o=s.count('0'),s.count('1')
    print(min(o,z+1))