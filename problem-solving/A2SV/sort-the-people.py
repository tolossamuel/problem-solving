class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(heights)):
            dic[heights[i]] = names[i]
        heights = sorted(heights, reverse = True)
        ans = []
        for i in heights:
            ans.append(dic[i])
        return ans