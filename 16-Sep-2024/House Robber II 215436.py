# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        dp = [0] * len(nums)
        last = nums[-1]
        
        for x in range(len(nums)-1,0,-1):
     
            temp = 0
            for y in range(x+2,len(nums)):
             
                temp = max(temp,dp[y])

                
            dp[x] = temp + nums[x]
 
        ans = 0
        for x in dp:
            ans = max(ans,x)
        dp = [0] * len(nums)
       
        
        for x in range(len(nums)-2,-1,-1):
            temp = 0
            for y in range(x+2,len(nums)):
                temp = max(temp,dp[y])
            dp[x] = temp + nums[x]
        for x in dp:
            ans = max(ans,x)
                
            

        return ans