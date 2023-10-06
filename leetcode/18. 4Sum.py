class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        list1 = set()
        for i in range(len(nums)-3):
            print(i)
            for y in range(i+1,len(nums)-2):
               
                first = y+1
                seconde = len(nums) - 1
                while(first<seconde):
                   
                    if (nums[first] + nums[seconde]+nums[i]+nums[y]) == target:
                        list1.add((nums[i], nums[y], nums[first], nums[seconde]))
                    if (nums[first] + nums[seconde]+nums[i]+nums[y]) > target:
                        seconde -= 1
                    else:
                        first += 1
        list1 = list(list1)
        return list1