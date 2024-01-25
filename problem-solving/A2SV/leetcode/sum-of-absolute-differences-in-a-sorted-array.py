class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = 0
        suf = sum(nums)
        ans = []
        n = len(nums)
        for i in range(n):
            pref += nums[i]
            suf -= nums[i]
            x = abs((nums[i]*(i+1)) - pref)
            x += abs((suf - (nums[i]*(n - i - 1))))
            # suf -= 
            ans.append(x)
        return ans
        