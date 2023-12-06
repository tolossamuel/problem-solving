n = input()
n = list(n)
m = n.count("?")
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = set(letter)

if m > 0:
	if (len(set(n))+m -1) != 26:
		print(-1)
	else:
		x = letter.difference(set(n))
		x = list(x)
		x.sort()
		for i in range(len(n)):
			if n[i] == "?":
				n[i] = x[0]
				
				x.pop(0)
		print("".join(n))
elif(m ==0):
	if (len(set(n))) != 26:
		print(-1)
else:
	print(123)
	x = letter.difference(set(n))
	x = list(x)
	for i in range(len(n)):
		if n[i] == "?":
			n[i] = x.pop(0)

	print("".join(n))


