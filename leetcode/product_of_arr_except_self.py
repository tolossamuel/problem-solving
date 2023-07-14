class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)
        postfix=1
        prefix=1
        for i in range(len(nums)):
            arr[i]=prefix
            prefix*=nums[i]
        for i in range(len(nums),0,-1):
            arr[i-1]*=postfix
            postfix*=nums[i-1]
        return arr