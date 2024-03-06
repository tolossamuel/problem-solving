class Solution:
    

    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        right = len(word) - 1
        forbidden = set(forbidden)
        ans = 0
        for left in range(len(word)-1,-1,-1):
            for k in range(left,min(left+10,right+1)):
                if word[left:k+1] in forbidden:
                    right = k - 1
                    break
            ans = max(ans,(right  - left +1))
        return ans