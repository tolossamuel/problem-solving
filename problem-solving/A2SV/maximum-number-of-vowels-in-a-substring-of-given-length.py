class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = k-1
        vowel = "aeiou"
        ans = 0
        for y in range(left,right+1):
            if s[y] in vowel:
                ans += 1
        temp = ans
        while(right < len(s)):
            if s[left] in vowel:
                temp -= 1
            left += 1
            right += 1
            if right >= len(s):
                return ans
            if s[right] in vowel:
                temp += 1
            ans = max(ans,temp)
        return ans