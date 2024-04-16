class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse = True)
        self.ans = []
        heapify(self.ans)
        for i in range(min(k,len(nums))):
            heappush(self.ans,nums[i])
        self.k = k
        print(self.ans)
    def add(self, val: int) -> int:
        if len(self.ans) < self.k:
            heappush(self.ans,val)
        elif self.ans[0] < val:
            heappop(self.ans)
            heappush(self.ans,val)
        return self.ans[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)