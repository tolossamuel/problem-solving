n,m = map(int,input().split())
l = list(map(int,input().split()))
s = input()
def sumOF(arr,n):
	
	arr.sort()
		
	
	return sum(arr[-n:])
	
sumOf = 0
counter = 1
if len(s) == 1:
	print(max(l))
else:
	for i in range(1,len(s)):

		if s[i] == s[i-1]:
			counter += 1
		else:
			if counter>m:
				sumOf += sumOF(l[i-counter:i],m)
			else:
				sumOf += sumOF(l[i-counter:i],counter)
			counter = 1
	else:
		
		
		if counter>m:
				sumOf += sumOF(l[i+1-counter:],m)
		else:
			sumOf += sumOF(l[i+1-counter:],counter)
		counter = 1


	print(sumOf)
		