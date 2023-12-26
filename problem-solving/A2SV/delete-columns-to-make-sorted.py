class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans = set()
        for i in range(1,len(strs)):
            for y in range(len(strs[i])):
                if strs[i][y] < strs[i-1][y]:
                    ans.add(y)               
            
        return len(ans)