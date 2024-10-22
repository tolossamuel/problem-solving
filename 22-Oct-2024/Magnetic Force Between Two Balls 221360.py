# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(n,k):
            val = position[0]
            k-=1
            _min = float("inf")
            for i in range(1,len(position)):
                if (val + n) <= position[i]:
                    _min = min(_min,position[i] - val)
                    val  = position[i]
                    k -= 1
               
            if k <= 0:
                return _min
            return float("inf")
        left = 1
        right = max(position)
        ans = 0
        while(left <= right):
            mid = (left + right)//2
            val = check(mid,m)
            if val != float("inf"):
             
                ans = max(ans,val)
                left = mid + 1
            else:
                
                right = mid - 1
        return ans


            