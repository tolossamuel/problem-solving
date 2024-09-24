# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = 1
        temp = 0
        nums.sort()
        x = len(nums)-1
        y = len(nums)-2
        
        while(y >= 0):

            temp += (nums[x] - nums[y])
            y -= 1
            if temp > k:
                ans = max(ans,(x-y - 1))
                dif = (x-y - 1)*(nums[x] - nums[x-1])
                x -= 1
                temp -= dif
        ans = max(ans,x+1)
        return ans

