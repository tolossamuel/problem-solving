class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        left = 0
        right = 0
        result = []
        if len(nums) < 3:
            return []
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            
            while left < right:
                sumOf = nums[i] + nums[left] + nums[right]
                if sumOf < 0:
                    left += 1
                elif sumOf>0:
                    right -= 1
                else:
                    if ([nums[i] , nums[left] , nums[right]]) not in result:
                        result.append([nums[i] , nums[left] , nums[right]])
                    left += 1
        
       
        return result

        