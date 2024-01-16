from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0 
        right = len(p)
        
        p = Counter(p)
        ans = []
        dic = defaultdict(int)
        dic = Counter(s[:right])
        while(right < len(s)):
            if dic == p:
                ans.append(left)
            dic[s[left]] -= 1
            dic[s[right]] += 1
            if dic[s[left]] == 0:
                dic.pop(s[left])
            left += 1
            right += 1
    
        if dic == p:
            ans.append(left)
        return ans
        
