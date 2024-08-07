class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
      
        g.sort()
        s.sort()
        left = 0
        right = 0
        counter = 0
        while(left < len(g) and right < len(s)):
            if g[left] <= s[right]:
                counter += 1
                right += 1
                left += 1
            else:
                right += 1
                
        return counter