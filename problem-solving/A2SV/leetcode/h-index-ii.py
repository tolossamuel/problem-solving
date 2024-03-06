class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)-1
        ans = 0
        while(left <= right):
            mid = (left + right)//2
            size = (len(citations) - mid)
            if citations[mid] >= size:
                # print(si)
                ans = max(ans,size)
                right = mid - 1
            else:
                ans = max(citations[mid],ans)
                left = mid + 1
        return ans