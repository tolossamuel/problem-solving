class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*len(days)
        dp[-1] = min(costs)
        for i in range(len(days)-2,-1,-1):
            next_7_day = days[i] + 6
            pos = bisect.bisect_right(days,next_7_day)
            next_7_day = costs[1]

            if pos < len(days):
                next_7_day += dp[pos]
            next_30_day = days[i] + 29
            pos = bisect.bisect_right(days,next_30_day)
            next_30_day = costs[2]
            if pos < len(days):
                next_30_day += dp[pos]
            dp[i] = min(next_30_day,next_7_day,dp[i+1]+costs[0])
        return dp[0]
    
