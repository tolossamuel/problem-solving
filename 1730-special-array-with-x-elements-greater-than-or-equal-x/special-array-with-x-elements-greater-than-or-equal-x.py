class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        dic = {}
        for i in range(len(nums)-1,-1,-1):
            r = 1
            if nums[i] in dic:
                r = dic[nums[i]][1]+1
            dic[nums[i]] = [len(nums) - i,r]
        t = len(nums)
        _max = nums[-1]
        for x in range(_max+1):
            if x == t:
                return x
            if x in dic:
                t -= dic[x][1]

        return -1

            
        return 2
                           
        