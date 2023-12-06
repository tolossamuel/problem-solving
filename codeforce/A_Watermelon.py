n = int(input())
ans = "NO"
if n <4:
	print("NO")

else:
	for i in range(2,n//2):
		if((n - i)%2 == 0):
			ans = "YES"
			break
print(ans)
