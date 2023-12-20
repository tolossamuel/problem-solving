class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if (nums[i]+nums[i-1] > nums[i-2]):
                if nums[i-1]+ nums[i-2] > nums[i]:
                    if nums[i] + nums[i-2] > nums[i-1] :
                        return (nums[i] + nums[i-1] + nums[i-2])
        return 0