class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        for i in range(len(score)):
            score[i] = [score[i],i]
        score.sort()
        ans = [""] * len(score)
        dic = {3:"Bronze Medal",2:"Silver Medal",1:"Gold Medal"}
        for i in range(len(score)):
            rank = len(score) - i
            if rank <= 3:
                ans[score[i][1]] = dic[rank]
            else:
                ans[score[i][1]] = str(rank)
        return ans
