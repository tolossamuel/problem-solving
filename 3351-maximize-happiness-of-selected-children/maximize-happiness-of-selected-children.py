class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        diff = 0
        while(happiness and k > 0):
            x = happiness.pop()
            if x >= diff:
                ans += (x-diff)
            else:
                return ans
            k-= 1
            diff += 1
        return ans