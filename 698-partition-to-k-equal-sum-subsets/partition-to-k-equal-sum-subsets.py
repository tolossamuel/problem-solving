class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        
        if k == 1:
            return True
        if k >= 11:
            return False 
        s = sum(nums)
        if s% k != 0:
            return False
        h = s//k
        for i in nums:
            if i > h:
                return False
        subset = [0]*k
        nums.sort(reverse = True)
        def solve(index):
            if index >= len(nums):
                return True
            for j in range(k):
                if subset[j] + nums[index] <= h:
                    subset[j] += nums[index]
                    if solve(index+1):
                        return True
                    subset[j] -= nums[index]
                    if subset[j] == 0:
                        break
            return False
      
        return solve(0)