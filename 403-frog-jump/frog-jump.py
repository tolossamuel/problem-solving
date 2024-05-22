class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        dp = defaultdict(set)
        for i in stones:
            dp[i]  = set()
        dp[stones[0]] = set([0])
        for x in stones:
            for j in dp[x]:
                d = [-1,0,1]
                for k in d:
                    nx = j + k

                    if nx + x in dp and nx != 0:
                        dp[nx+x].add(nx)
        if dp[stones[-1]]:
            return True
        return False
            

            
