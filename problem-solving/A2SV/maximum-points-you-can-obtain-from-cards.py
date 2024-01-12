class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = 0
        n = len(cardPoints) - k
        ans = 0
        temp = 0
        index = n
        count = 0
        for i in range(n,len(cardPoints)+k):
            temp += cardPoints[i%len(cardPoints)]
            count += 1
            if count >= k:
                ans = max(ans,temp)
                temp -= cardPoints[index%len(cardPoints)]
                index += 1
        return ans
            
