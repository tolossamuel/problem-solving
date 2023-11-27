dic = {}
value = []


s = "dztz"
shifts = [[0,0,0],[1,1,1]]
for i in range(len(s)):
	value.append(ord(s[i]))
for i in range(97,122+1):
	dic[i] = chr(i)

for i in shifts:
	for y in range(i[0],i[1]+1):
		if (i[2]==0):
			value[y] -= 1
		else:
			value[y] += 1
ans = ""
for i in value:
	if i < 97:
		ans += (dic[123 - (97 - i)])
	elif (i > 122):
		ans += (dic[96 - (i - 122)])
	else:
		ans += (dic[i])
print(ans)