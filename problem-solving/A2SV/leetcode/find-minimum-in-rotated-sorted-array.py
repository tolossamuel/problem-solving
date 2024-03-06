class Solution:
    def findMin(self, nums: List[int]) -> int:
        x = nums[0]
        left = 1
        right = len(nums)-1
        while(left <= right):
            mid = (left + right)//2
            if nums[mid] > x:
                left = mid + 1
            elif nums[mid] < x:
                x = nums[mid]
                right = mid - 1
           
        # print(x)
        return x