class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        left = 1
        right = 1+1
        counter = 0
        while(right < len(nums)):
            if (nums[left] < nums[left-1]):
                if nums[left-1] <= nums[right]:
                    nums[left] = nums[left]
                else:
                    nums[left-1] = nums[left]
                counter += 1
            # print(nums)
            if nums[left] > nums[right]:
                if nums[left-1] <= nums[right]:
                    nums[left] = nums[left-1]
                else:
                    nums[right] = nums[left]
                counter += 1
            left += 1
            right += 1
        if counter <= 1:
            return True
        return False