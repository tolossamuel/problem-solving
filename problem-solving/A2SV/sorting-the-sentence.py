class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s  = s.split(" ")
        ans = ["0"]*len(s)
        for i in s:
            ans[int(i[-1])-1] = i[:len(i)-1]
        ans = " ".join(ans)
        return ans