
try:
    t = int(input())
except Exception as e:
    print(e)
p1 = 0
p2 = 0
lead = 0
leader = 0
for game in range(t):
    scores = [int(score) for score in input().split()]
    p1 += scores[0]
    p2 += scores[1]
    thislead = p1 - p2
    if thislead < 0:
        thisleader = 2
    else:
        thisleader = 1
    if abs(thislead) > lead:
        lead = abs(thislead)
        leader = thisleader
print(f'{leader} {lead}')