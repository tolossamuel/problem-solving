class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = 2e31
        right = 2e31
        for i in nums:
            if right < i:
                return True
            elif left >= i:
                left = i
            else:
                right  = i
        return False
        # [1,2,0,4,5]
        
        
        