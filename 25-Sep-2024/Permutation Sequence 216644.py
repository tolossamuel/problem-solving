# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = list(range(1, n + 1))
        
        for i in range(1, n):
            fact *= i
        
        ans = []
        k -= 1
        
        while True:
            ans.append(str(nums[k // fact]))
            nums.pop(k // fact)
            
            if not nums:
                break
            
            k %= fact
            fact //= len(nums)
        
        return ''.join(ans)
