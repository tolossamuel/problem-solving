class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candels = []
        pref = []
        _sum = 0
        ans = []
        for i in range(len(s)):
            if s[i] == "|":
                candels.append(i)
                pref.append(_sum)
                _sum = 0
            else:
                if candels:
                    _sum += 1
        pref.append(0)
        for i in range(1,len(pref)):
            pref[i] += pref[i-1]
        for i in range(len(queries)):
            left = bisect.bisect_left(candels,queries[i][0])
            right = bisect.bisect_left(candels,queries[i][1])
            if right >= len(candels)  or (queries[i][1] < candels[right]):
                right -= 1
            if left >= right:
                ans.append(0)
            else:
                _sum = pref[right] - pref[left]
                ans.append(_sum)
        return ans