class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left = 0
        right = len(p)-1
        s = list(s)
        p = list(p)
        p.sort()
        result = []
        for i in range(len(s)):
            
            if sorted(s[left:right+1]) == p:
                
                result.append(left)
            left += 1
            right += 1
        return result
        