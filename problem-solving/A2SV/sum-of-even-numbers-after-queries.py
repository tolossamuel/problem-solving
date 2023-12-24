class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        s = sum(a for a in nums if a%2 == 0)
        ans = []
        for i,y in queries:
            if nums[y]%2 == 0:
                s -= nums[y]
            nums[y] += i
            if nums[y] %2 == 0:
                s += nums[y]
            ans.append(s)
        return ans
