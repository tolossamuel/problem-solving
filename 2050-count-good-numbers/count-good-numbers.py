class Solution:
    
    def countGoodNumbers(self, n: int) -> int:
        Mod =  10**9 + 7
        if n%2 == 0:
            return pow(20,n//2,Mod)
        else:
            return (5 * self.countGoodNumbers(n-1))%Mod