class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums)-1
        counter = 0
        while (left< right):
            # print(left,right,nums,(nums[left] + nums[right]))
            if (nums[left] + nums[right]) == k:
                # print(left,right,nums,"r")
                counter += 1
                
                nums.pop(left)
                right -= 1
                nums.pop(right)
                right -= 1
                
            elif (nums[left]+ nums[right]) > k:
                right -= 1
            else:
                left += 1
        return counter
            