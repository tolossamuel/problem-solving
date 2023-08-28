n = int(input())
p = []
for i in range(0, n):
	p.append(int(input()))
best = 1
for i in range(0, n):
	count = 1
	x = p[i]
	while x != -1:
		count += 1
		x = p[x - 1]
	if count > best:
		best = count
print(best)