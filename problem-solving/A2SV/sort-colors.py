class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Initialize pointers for the three colors: red (0), white (1), and blue (2)
        red, white, blue = 0, 0, len(nums) - 1
        
        while white <= blue:

            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            # If the current element is 1, move the white pointer to the right
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1