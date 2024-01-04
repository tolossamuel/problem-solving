class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
  
        
        if len(nums) <=2 :
            return 0
        nums.sort()
        left = 0
        right = len(nums)-1
        ope = 0
        while(left < right):
            if ((nums[right]+nums[left]) == k):
                nums.pop(right)
                nums.pop(left)
                
                
                right -= 2
                ope += 1
            elif ((nums[right]+nums[left]) < k):
                left += 1
            else:
                right -= 1
        return ope
        
            