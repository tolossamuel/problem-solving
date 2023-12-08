class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)-1,-1,-1):
          if nums[i]>nums[i-1]:
            p = i
            break
        if p>0:
          nums[p:] = sorted(nums[p:])
          for i in range(p,len(nums)):
            if nums[i]>nums[p-1]:
              nums[i],nums[p-1] = nums[p-1],nums[i]
              break
        else:
          nums.reverse()
        print(nums)