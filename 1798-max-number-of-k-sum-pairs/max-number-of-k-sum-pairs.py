class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left =0
        right = len(nums)-1
        counter = 0
        while(left < right):
            val = nums[left] + nums[right]
            if val == k:
                counter += 1
                left += 1
                right -= 1
            elif val > k:
                right -= 1
            elif val < k:
                left += 1
        return counter
    