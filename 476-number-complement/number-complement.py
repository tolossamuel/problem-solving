class Solution:
    def findComplement(self, num: int) -> int:
        ans = log(num)/log(2)
        
        ans = ceil(ans)
        # print(ans)
        if num == (2**ans):
            ans += 1
        ans = (2**ans) - 1
        ans = ans^num
        return ans