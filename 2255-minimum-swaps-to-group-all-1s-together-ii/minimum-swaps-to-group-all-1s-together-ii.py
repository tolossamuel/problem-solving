class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one = nums.count(1)
        nums += nums
        if one == 0:
            return 0
        zero = 0
        n = 0
        right = 0
        left = 0
        ans = len(nums)
        while(right < len(nums)):
            if n == one:
                ans = min(ans,zero)
                if nums[left] == 0:
                    zero -= 1
                left += 1
                right += 1
                n -= 1
            else:
                if nums[right] == 0:
                    zero += 1
                n += 1
                if n != one:
                    right += 1
        return ans
            