class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return ((nums[0]+nums[1])%10)
        def sumOf(arr):
            sumOfArr = []
            for i in range(len(arr)-1):
                ans = arr[i]+arr[i+1]
                sumOfArr.append(ans%10)
            if len(sumOfArr) <= 1:
                return sumOfArr
            else:
                return sumOf(sumOfArr)
        ans = sumOf(nums)
        print(ans)
        return ans[0]
