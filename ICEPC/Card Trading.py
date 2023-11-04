n, t, k = map(int, input().split())
deck = [0] * (2 * 10 ** 5 + 3)
cards = []
trans = [0] * t
acc = [0] * t

for x in map(int, input().split()):
    deck[x - 1] += 1

for _ in range(t):
    cards.append(tuple(map(int, input().split())))

for i in range(t):
    trans[i] = (cards[i][0] * (2 - deck[i]), cards[i][1] * deck[i])

ans = 0

for i in range(t):
    ans -= trans[i][0]
    acc[i] = trans[i][0] + trans[i][1]

acc.sort()

for i in range(k, t):
    ans += acc[i]

print(ans)
