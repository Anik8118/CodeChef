a, b = map(float, input().split())
if a % 5 == 0 and a + 0.50 <= b:
    print(b - a - 0.50)
else:
    print(b)
    