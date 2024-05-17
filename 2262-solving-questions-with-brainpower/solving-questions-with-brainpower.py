class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]
        for i in range(len(questions)-2,-1,-1):
            dp[i] = questions[i][0]
            s = i+questions[i][1]+1
            if s < len(dp):
                dp[i] += dp[s]
            dp[i]  = max(dp[i],dp[i+1])
           
        return max(dp)

