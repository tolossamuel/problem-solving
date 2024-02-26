class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = 1
        pos = nums[0]
        while(x < len(nums)):
            if pos == 0:
                return False
            
            pos = max(pos-1,nums[x])
            x += 1
        return True
