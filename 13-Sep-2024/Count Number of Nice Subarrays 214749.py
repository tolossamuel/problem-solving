# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        count = 0
        curent = 0
        for right in range(len(nums)):
            
            if nums[right]%2 == 1:
                    count += 1
                    curent = 0 
                
            while(count == k):

                
                if nums[left]%2 == 1:
                    count -= 1
                curent += 1
                left += 1
            ans += curent
     
        return ans
            