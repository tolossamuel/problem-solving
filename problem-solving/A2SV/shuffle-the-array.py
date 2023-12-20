class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # [2,5,1,3,4,7]
        # [2,3,5,1,4,7]
        # [2,3,5,4,1,7]
        list1 = []
        for i in range(n):
            list1.append(nums[i])
            list1.append(nums[n+i])
            
        return list1

        