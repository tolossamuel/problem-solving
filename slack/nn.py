left = 0
s = "abc"
right = len(s)-1
counter = 0
s = list(s)
while (left < right):
	
	if s[left] != s[right] and counter != 1:
		if s[right -1 ]!= s[left]:
			s.pop(left)
			left -= 1
			
		elif s[left + 1 ]!= s[right]:
			s.pop(right)
			left -= 1
			
		elif s[left]!= s[right] and left+1 == right:
			s.pop(left)
			left -= 1
			
			
		else:
			print(False)
		counter += 1
		print(s,counter,right,left)
	elif s[left] != s[right]:
			print(False)
	left += 1
	right -= 1
	print(left,right)
print(True)
