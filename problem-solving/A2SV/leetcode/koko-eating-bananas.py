class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(hour,amount):
            for i in range(len(piles)):
                x = piles[i]
                hour -= ceil(x/amount)
            if hour >= 0:
                return True
            return False
        right = max(piles)
        left = 1
        ans = 0
        while(left <= right):
            mid = (left + right )//2
            if check(h,mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans