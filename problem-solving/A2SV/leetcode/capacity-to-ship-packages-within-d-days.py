class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mass,day):
            x = 0
            for i in range(len(weights)):
                
                if (x + weights[i]) <= mass:
                    x += weights[i]
                else:
                    if weights[i] > mass:
                        day = -1
                        break
                    day -= 1
                    x = weights[i]
            day -= 1
            if day >= 0:
                return True
            return False
        lar = sum(weights)
        small = min(weights)
        ans = 0
        while(small <= lar):
            mid = (lar + small)//2
            if check(mid,days):
                ans = mid
                lar = mid - 1
            else:
                small = mid + 1
        return ans
