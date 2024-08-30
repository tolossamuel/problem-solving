class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        pos = [0,len(nums)-1]
        while(left <= right):
            mid = (left + right)//2
            if nums[mid] < target:
                pos[0] = mid+1
                left = mid + 1
            else:
                right = mid - 1




        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = (left + right)//2
            if nums[mid] > target:
                pos[1] = mid-1
                right = mid - 1
            else:
                left = mid + 1
                
        if pos[0] > pos[1]:
            return [-1,-1]
        return pos