class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        dic = defaultdict(int)
        while(right < len(s)):
            if dic[s[right]] >=1:
                ans = max(ans, (right - left))
                # print(ans,left,right)
                left += 1
                right = left
                dic = defaultdict(int)
                # ans = max(temp)

            else:
                dic[s[right]] += 1
                right += 1
 
        ans = max(ans,(right-left))

       
        return ans
