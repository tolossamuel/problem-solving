
class Solution:
    def balancedString(self, s: str) -> int:
        def checker(dic,n):
            if max(dic.values()) > n:
                return False
            return True
        dic  = Counter(s)
        left = 0
        right = 0
        ans = float("inf")
        n = len(s)//4
        if checker(dic,n):
            return 0
        while(right < len(s)):
            dic[s[right]] -= 1
            right += 1
            
            while(checker(dic,n) and left < len(s)):
                ans  = min(ans,(right-left))
                dic[s[left]] += 1
                left += 1

            
        return ans 