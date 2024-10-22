# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        _min = float("inf")
        _max = float("-inf")
        arr = []
        for x in arrays:
            for y in x:
                _min = min(_min,y)
                _max = max(_max,y)
            arr.append([_min,_max])
            _min = float("inf")
            _max = float("-inf")
        cur_x = arr[0][0]
        cur_y = arr[0][1]
        ans = 0
        for x,y in arr[1:]:
            
            ans = max(ans,abs(cur_y - x), abs(y - cur_x))
            cur_y = max(cur_y,y)
            cur_x = min(cur_x,x)


        return ans