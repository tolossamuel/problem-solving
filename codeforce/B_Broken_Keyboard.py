n = int(input())
for y in range(n):
	s = input()
	r = ""
	
	if not s:
		print("")
	elif len(s) == 1:
		print(s)
	else:
		
		for i in range(len(s)):
			if i +1 == len(s):
				if (s[i] != s[i-1]):
					r+= s[i]
			elif i > 0:
				if (s[i] != s[i+1] and s[i] != s[i-1]):
					r += s[i]
			elif i == 0:
				if (s[i] != s[i+1]):
					r += s[i]

			
		


		r = set(r)
		r = list(r)
		r.sort()

		r = "".join(r)
		print(r)



		# https://codeforces.com/gym/487945/my