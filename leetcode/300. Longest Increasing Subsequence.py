def subsequence(arr,left,right,result,sumOf,checker):
	if right>= len(arr):
		
		sumOf = max(sumOf,len(result))
		print(result)
		if checker:
			result.pop()
			right = checker[-1]+1
			checker.pop()
			print(right)
			print(result)
			return subsequence(arr,left,right,result,sumOf,checker)
		return subsequence(arr,left+1,left+1,[],sumOf,[])
		
	elif left+1 >= len(arr):
		
		return sumOf
	else:
		
		if not result:
			result.append(arr[right])
		elif result[-1]< arr[right]:
			
			result.append(arr[right])
			checker.append(right)

		return subsequence(arr,left,right+1,result,sumOf,checker)
nums = [0,1,0,3,2,3]
ans = subsequence(nums,0,0,[],0,[])
print("ans")
print(ans)