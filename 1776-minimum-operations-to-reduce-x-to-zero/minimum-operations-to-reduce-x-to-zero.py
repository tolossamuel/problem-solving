class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        _sum = sum(nums)
        if x > _sum:
            return -1
        if x == _sum:
            return len(nums)
        prefix = [0]
        dic = {0:0}
        for i in nums:
            prefix.append(i + prefix[-1])
        prev = 0
        for i in range(len(nums)-1,-1,-1):
            dic[nums[i]+prev] = dic[prev]+1
            prev += nums[i]
        _min = float("inf")
        for i in range(len(prefix)):
            dif = x - prefix[i]
            if dif in dic:
                left = i
                left += dic[dif]
                _min = min(left,_min)
        return _min if _min != float("inf") else -1
    