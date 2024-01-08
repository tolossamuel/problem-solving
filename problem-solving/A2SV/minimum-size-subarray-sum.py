class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        y = 0
        temp = 0
        ans = 10e6
        while(x < len(nums)):
            if y >= len(nums) and temp < target:
                break
            if temp >= target:
                temp -= nums[x]
                ans = min(ans,(y-x))
                x += 1
            else:
                temp += nums[y]
                y += 1
            # print(temp,ans)
        return ans if ans < 10e6 else 0