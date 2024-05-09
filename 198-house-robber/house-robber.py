class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:

            return nums[0]
        dic = defaultdict(int)
        dic[len(nums)-1] += nums[-1]
        dic[len(nums)-2] += nums[-2]
        for i in range(len(nums)-3,-1,-1):
            dic[i] += (nums[i] + max(dic[i+3],dic[i+2]))
            # print(dic)
        return max(dic[0],dic[1])