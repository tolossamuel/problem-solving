class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counter ={}
        for i in nums:
            counter[i] = 0
        for i in nums:
            counter[i] += 1
        result = set()
        for i in nums:
            if counter[i] > (n/3):
                result.add(i)

        return list(result)