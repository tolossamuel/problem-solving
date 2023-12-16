class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left,right,ans = 0,(len(nums)+1)//2,0
        while(right < len(nums)):
            if nums[right] > nums[left]:
                right += 1
                left += 1
                ans += 2
            else:
                right += 1
        return len(nums) - ans