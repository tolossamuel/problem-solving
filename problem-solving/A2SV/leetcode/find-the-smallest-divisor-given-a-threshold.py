class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def cal(divisor):
            counter = 0
            for i in nums:
                counter += ceil(i/divisor)
            return counter


        right = max(nums)
        left = 0
        ans = 0
        counter = 0
        while(left <= right):
            mid = (left + right)//2
            if mid == 0:
                left = 1
            elif cal(mid) <= threshold:
                ans = mid
                right  = mid - 1
            else:
                left = mid + 1
        return ans
            
        