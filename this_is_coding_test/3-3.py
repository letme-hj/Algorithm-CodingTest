n, m = map(int, input().split())
cards = []
for row in range(n):
    cards.append(list(map(int, input().split())))

candidates = []
for row in cards:
    candidates.append(sorted(row)[0])
print(sorted(candidates)[-1])
