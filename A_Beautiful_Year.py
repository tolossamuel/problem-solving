n = int(input())


n += 1
while (len(set(list(str(n)))) != len(list(str(n)))):
	   n += 1;
print(n)
