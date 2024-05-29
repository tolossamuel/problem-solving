class Solution:
    
    def maxProduct(self, words: List[str]) -> int:
        heap = {}
        for x in range(len(words)):
            heap[x] = set(list(words[x]))
        ans = 0
        for x in range(len(words)):
            for y in range(x+1,len(words)):
                union = len(heap[x].intersection(heap[y]))
                if union == 0:
                    ans = max(ans,len(words[x]) * len(words[y]))
        return ans
