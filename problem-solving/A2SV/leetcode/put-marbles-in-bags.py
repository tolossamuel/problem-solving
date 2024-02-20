class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        ans = []
        for i in range(1,len(weights)):
            ans.append(weights[i] + weights[i-1])
        ans.sort()
        _min = sum(ans[:k-1])
        _max = sum(ans[len(ans) - k+1:])
        # print(ans,_min,_max)
        return (_max - _min)