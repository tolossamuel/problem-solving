class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = [0] * n
        for x,y in roads:
            counter[x] += 1
            counter[y] += 1
        print(counter)
        counter.sort()
        mul = 1
        ans = 0
        print(counter)
        for x in counter:
            ans += (x*mul)
            mul += 1
        return ans
