class Solution:
    def partitionString(self, s: str) -> int:
        sets = set()
        ans = 0
        for x in s:
            if x not in sets:
                sets.add(x)
            else:
                ans += 1
                sets = set([x])
        if sets:
            ans += 1
        return ans