class Solution:
    def integerBreak(self, n: int) -> int:
        catch = {}
        def solve(n,mul,num,k):
            
            if n < 0:
                return float("-inf")
            if n == 0:
                return mul if k >= 2 else float("-inf")
           
            if num > n:
                return float("-inf")
            if ((n,mul,num) in catch):
                return catch[(n,mul,num)]
            ans = 0
            
            ans = max(
                ans,
                solve(n,mul,num +1,k),
                solve(n - num,mul * num,num,k+1),

            )
            catch[(n,mul,num)] = ans
            return ans
        return solve(n,1,1,0)
        