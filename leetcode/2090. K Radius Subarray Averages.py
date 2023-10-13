class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left = 2*k
        right = 0
        n = len(nums)
        print(n)
        result = [-1]*n
        print(result)
        sum_of = 0
        if (2*k)<n:
            sum_of = sum(nums[right:left+1])
            result[((left+right)//2)] = sum_of//((2*k)+1)
        while(left < len(nums)):
            
            sum_of -= nums[right]
            right += 1
            left += 1
            if (left < n):
                sum_of += nums[left]
                result[((left+right)//2)] =sum_of//((2*k)+1)
                
        return result