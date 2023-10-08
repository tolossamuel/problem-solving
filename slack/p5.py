diff = []
nums = [1,5,9,1,5,9,6]
indexDiff = 5
valueDiff = 10
for i in range(indexDiff+1):
	print(i,i)
	diff.append([i,indexDiff-i])
	diff.append([i,indexDiff+i])
	temp = indexDiff -i - 1
	while(temp > i):
		diff.append([i,temp])
		temp = temp - 1
for i in diff:
	if(i[0]!=i[1] and abs(i[0] - i[1]) == valueDiff):
		print(True)
		exit()
print(False)
print(diff)
