class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value = set()
        counter = 0
        nums.sort(reverse = True)
        if len(nums) >= 3:
            for i in range(len(nums)):
                if nums[i] not in value:
                    if counter ==2:
                        return nums[i]
                    else:
                        value.add(nums[i])
                        counter += 1
            
            return nums[0]
        else:
            return nums[0]
            