class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        pos = 0
        while(left <= right):
            mid = (left + right)//2
            if nums[mid] < target:
                pos = mid+1
                left = mid + 1
            else:
                right = mid - 1
        return pos