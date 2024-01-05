class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # the questions is abut sum of three num in the array that closest to num
        # [-1,2,1,-4]// array
        # target = 1
        # three num from array like [-1,2,1] = 2, [-1,1,-4] = -4, [-1,2,-4] = -3,
        # [1,2,-4] = -1 ...
        # -5,-4,-3,-2,-1,0,1,2,3,4,5
        sum_nums = nums[0] + nums[1] + nums [-1]
        # we sort the array
        # [-4,-1,1,2] target = 1
        nums.sort()
        first_nums,second_nums=0,0
        for  i in range(len(nums)-2):
            first_nums = i+1
            last_nums = len(nums) -1
            while(first_nums < last_nums):
               
                sum_curent = (nums[i] + nums[last_nums] + nums[first_nums])
                if (sum_curent) < target:
                    first_nums += 1
                else:
                    last_nums -= 1
                if abs(target - sum_curent) < abs(target - sum_nums):
                    sum_nums = sum_curent
        return sum_nums
            
        