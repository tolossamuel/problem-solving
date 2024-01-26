class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        s = sum(nums)
        R = s % p
        if s < p:
            return -1
        if R == 0:
            return 0
        pref_sum = [0]*(n+1)
        for i in range(1, n+1):
            pref_sum[i] = pref_sum[i-1] + nums[i-1]
        
        count = {}
        ans = float('inf')
        for i in range(n+1):
            if pref_sum[i] % p in count:
                ans = min(ans, i - count[pref_sum[i]%p])
            a = pref_sum[i] % p
            count[(R + a) %p] = i

        if ans == n:
            return -1

        return ans if ans < float('inf') else -1