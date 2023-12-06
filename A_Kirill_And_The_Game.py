s = "NO"
n = list(map(int,input().split()))
for i in range(n[2],n[3]+1,+1):
	if i*n[4] <= n[1] and i*n[4] >= n[0]:
		s = "YES"
		break
print(s)
