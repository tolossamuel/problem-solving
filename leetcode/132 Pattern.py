class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
            
        stack = []
        comp = float('-inf')

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < comp:
                return True
            while stack and nums[i] > stack[-1]:
                comp = stack.pop()
            stack.append(nums[i])

        return False
       
	   