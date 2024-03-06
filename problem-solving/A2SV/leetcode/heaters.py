class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = float("-inf")
        for i in range(len(houses)):
            x = bisect.bisect_left(heaters,houses[i])
            left = float("inf")
            if x > 0:
                left =  houses[i]  - heaters[x-1]
            right = float("inf")
            if x < len(heaters):
                right = heaters[x] - houses[i] 
            temp = min(left,right)
            # print(temp)
            ans = max(temp,ans)
        return ans