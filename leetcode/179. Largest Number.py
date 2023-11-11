class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # the problem is sort the number to create big numbers as possibles
        # [10,2]
        # in this test case there are two way to create numbers the first one is 102 and 210 so 210 is greater than  102
        # the sorting key is sort base on the first number  10, 2 to sort 2 is greater than 1 so we sorted it to 210
        # [3,30,34,5,9] for this test case 9 is greater than 3,3,3,and 5 [9]
        # [9,3,30,34,5] check 5 is greater than 3,3,3,
        # [9,5,3,30,34] 3 is equal to 3,3 check the next index of the number that means 34 next index is 4 so 4 is greater then 3,0
        # [9,5,34,3,30] and 3 is equal to 3 so check next index 0 is lethan 3 so 
        # [9,5,34,3,30] 
        # "45","46" = >
        def supportive(x,y):
            z = x+y
            y = y+x
            if z> y:
                return True
            else:
                return False

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        for i in range(len(nums)-1):
            for y in range(i+1,len(nums)):
                if not (supportive(nums[i],nums[y])):
                    nums[i],nums[y] = nums[y],nums[i]
        string = "".join(nums)
        if string.count("0") == len(string):
            return "0"
        return string

