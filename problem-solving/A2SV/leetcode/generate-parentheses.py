class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def helper(s,n,l,r):
            if len(s) == (2*n):
                ans.append(s)
                return []
            if l < n:
                helper(s+"(",n,l+1,r)
            if l > r:
                helper(s+")",n,l,r+1)
            
        helper("",n,0,0)

        return ans