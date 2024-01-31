class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        prefix = [0 for i in range(len(nums) + 1)]
        Mod =  10**9 + 7
        ans = 0
        for l, r in requests:
            prefix[l] += 1
            prefix[r + 1] -= 1

        prefix = list(accumulate(prefix))

        prefix.sort(reverse = True)
        nums.sort(reverse = True)

        for i in range(len(nums)):
            ans += prefix[i]*nums[i]

        return ans % Mod

        