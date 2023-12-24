class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
       
     
        nums.sort()

        counter = 1
        ans = 0
        for i in range(1,len(nums)):
            if (nums[i]-1) == nums[i-1]:
                
                counter += 1
            elif nums[i] != nums[i-1]:
                ans = max(counter,ans)
                counter = 1
        ans = max(counter,ans)
        return ans
        