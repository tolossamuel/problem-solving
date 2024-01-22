class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0] = 1
        ans = 0
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            x  = _sum - k
            if x in dic:
                ans += dic[x]
            if _sum in dic:
                dic[_sum] += 1
            else:
                dic[_sum] = 1
        return ans