# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = [0] * 11
    for x in a:
        freq[x] += 1
    print(n - max(freq))