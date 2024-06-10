class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        checker = sorted(heights)
        counter = 0
        for x in range(len(heights)):
            if heights[x] != checker[x]:
                counter += 1
        return counter