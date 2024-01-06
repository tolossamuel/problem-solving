class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        val = sum(nums[0:k])
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[-1]+nums[i])
     
        for i in range(len(nums)-k+1):
            if i == 0:
                sumOf = pre[k-1+i]
               
            else:
                sumOf = (pre[k-1+i] - pre[i-1])

            val = max(val,sumOf)
        return float(val)/k
