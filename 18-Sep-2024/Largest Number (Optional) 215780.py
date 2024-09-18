# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for y in range(len(nums)):
            for i in range(y+1,len(nums)):
                
                if int(nums[y] + nums[i]) < int(nums[i] + nums[y]):
                    nums[y],nums[i] = nums[i],nums[y]
        
        x = "".join(nums)
        x = int(x)
        

        return str(x)