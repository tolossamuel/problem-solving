class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse = True)
        self.ans = nums[:k]
    
        heapify(self.ans)
        self.k = k
    def add(self, val: int) -> int:

        if len(self.ans) < self.k:
            heappush(self.ans,val)
        else:
            if self.ans[0] < val:
                heappop(self.ans)
                heappush(self.ans,val)
        return self.ans[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)