def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        happy = True
        count = [0] * (n + 1)

        for _ in range(n):
            groupSizePreference = int(input())
            count[groupSizePreference] += 1

        for j in range(2, n + 1):
            if count[j] % j != 0:
                happy = False

        if happy:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
