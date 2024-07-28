for _ in range(int(input())):
    n, a, b = map(int, input().split())
    rounds = n.bit_length() - 1
    print((rounds-1)*(a+b) + a)