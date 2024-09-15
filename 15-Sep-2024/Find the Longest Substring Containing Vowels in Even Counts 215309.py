# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                l=(s[j:j+i])
                odd = 0
                for k in "aeiou":
                    if(l.count(k)%2!=0):
                        odd = True
                        break
                if(not odd):
                    return (i)
        return 0