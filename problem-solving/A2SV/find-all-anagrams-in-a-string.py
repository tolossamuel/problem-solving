class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0 
        right = len(p)-1
        p = list(p)
        p.sort()
        ans = []
        while(right < len(s)):
            temp = list(s[left:right+1])
            temp.sort()
            if temp == p:
                ans.append(left)
            left += 1
            right +=1
        return ans
        
