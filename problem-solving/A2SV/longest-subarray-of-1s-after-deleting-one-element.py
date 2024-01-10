class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if set(nums) == (1):
            return len(nums)-1
        count = 0
        left = 0
        right = 0
        index = 0
        ans = 0
        while(right < len(nums)):
            if nums[right] == 0:
                count +=1
                if count != 2:
                    index= right
            if count == 2:
                ans = max(ans,(right - left-1))
                left = index+1
                index = right
                
                count = 1
                right += 1
            else:                
                right += 1
        ans = max(ans,(right-left-1))
        return ans


