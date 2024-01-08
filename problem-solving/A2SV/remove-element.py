class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = 0
        while(right < len(nums) and left < len(nums)):
            # print(left)
            if nums[left]!= val:
                left += 1
                right = left
            elif nums[right] == val:
                right += 1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                right += 1
                left += 1
        return left 