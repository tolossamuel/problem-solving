class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = len(nums)-1
        z = 0
        while(z <= y):
            if nums[z] == 0:
                nums[x],nums[z] = nums[z],nums[x]
            if nums[z] == 2:
                nums[y],nums[z] = nums[z],nums[y]
                z -= 1
                
            if nums[x] == 0 and (x+1) <= z:
                x += 1
            if nums[y] == 2:
                y -= 1
            z += 1 
          
        # print(nums)
