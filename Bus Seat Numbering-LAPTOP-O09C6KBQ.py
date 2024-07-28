for _ in range(int(input())):
    x=int(input())
    if x in [1,3,5,7,9,2,4,6,8,10]:
        print("Lower Double")
    elif x in [11,12,13,14,15]:
        print("Lower Single")
    elif x in [16,18,20,22,24,17,19,21,23,25]:
        print("Upper Double")
    else:
        print("Upper Single")