class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg_index = 1
        pos_index = 0
        val = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                val[pos_index] = nums[i]
                pos_index += 2
            else:
                val[neg_index] = nums[i]
                neg_index += 2
        return val