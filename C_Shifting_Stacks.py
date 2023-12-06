
def isSorted(arr,n):
	if n >= len(arr):
		return True
	return arr[n] >arr[n-1] and isSorted(arr,n+1)
def isSortedIncreasing(arr,n):
	if n >= len(arr):
		return True
	return arr[n] <arr[n-1] and isSorted(arr,n+1)
def isEqual(arr,n):
	if n >= len(arr):
		return True
	return arr[n] == arr[n-1] and isEqual(arr,n+1)
n = int(input())
for i in range(n):
	x = int(input())
	l = list(map(int,input().split()))
	l.sort()
	if isSortedIncreasing(l,1) or isSorted(l,1) or isEqual(l,1):
		print("YES")
	else:
		print("NO")