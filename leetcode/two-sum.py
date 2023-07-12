class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listt=[]
        for i in range(len(nums)-1):
            for y in range(i+1,len(nums)):
                if(nums[i]+nums[y]==target):
                    listt.append(i)
                    listt.append(y)
                    return listt
        return -1