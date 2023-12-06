def check(arr,n,m):
	if n == m:
		return True
	if not arr:
		return True
	arr2 = arr[-len(arr):-1]
	if arr == arr[::-1]:
		return True
	elif arr[1:] == arr[0:-1]:
		return True
	
	elif arr[:len(arr)-1] == arr2:
		return True
	
	return (True and check(arr[n:m],n+1,m-1))
	
arr =[1,2,3]


print(check(arr,0,3))