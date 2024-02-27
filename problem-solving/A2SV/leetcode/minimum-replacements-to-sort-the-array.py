class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        _max = nums[-1]
        counter = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > _max:
                x = ceil(nums[i]/_max)
                counter += x-1
                _max = (nums[i]//x)
                # print(counter,nums[i],"=====")
            else:
                _max = nums[i]
               
        return counter