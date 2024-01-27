class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        dic[0] += 1
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        ans = 0
        for i in nums:
            ans += dic[(i-goal)]
            dic[i] += 1
        return ans
