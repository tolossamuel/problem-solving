n = int(input())
for i in range(n):
	m = int(input())
	l = list(map(int, input().split()))
	x = list(l)
	x.sort()
	for i in range(m-1):
	
		for y in range(i+1,m,+1):
			if x[i] == l[i]:
				
				break
			else:
				if l[i] != l[y]:
					
					if l[i]%2 == 0 and l[y]%2 == 0:
						if l[i] > l[y]:
							l[i], l[y] = l[y], l[i]
					elif l[i]%2 != 0 and l[y]%2 != 0:
						if l[i] > l[y]:
							l[i], l[y] = l[y], l[i]
	if l == x:
		print("YES")
	else:
		print("NO")


























	# if x == l:
	# 	print("YES")
	# else:
	# 	if (len(set(x)) == m):
			
	# 		if x[0]%2 != 0 and l[0]%2== 0:
	# 			print("NO")
	# 		elif x[0]%2 == 0 and l[0]%2!= 0:
	# 			print("NO")
	# 		else:
	# 			print("YES")
	# 	else:
	# 		if x[0]%2 != 0 and l[0]%2== 0:
	# 			print("NO")
	# 		elif x[0]%2 == 0 and l[0]%2!= 0:
	# 			print("NO")
	# 		else:
	# 			print("YES")
			

					