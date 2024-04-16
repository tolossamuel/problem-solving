class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        heapq.heapify(self.heap1)
        heapq.heapify(self.heap2)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap1,num)
        x = len(self.heap2)
        while(self.heap2 and -self.heap2[0] > self.heap1[0] ):
            x = heapq.heappop(self.heap2)
            heapq.heappush(self.heap1,-x)
            x = heapq.heappop(self.heap1)
            heapq.heappush(self.heap2,-x)
        if len(self.heap1) > len(self.heap2):
            x = heapq.heappop(self.heap1)
            heapq.heappush(self.heap2,-x)
    def findMedian(self) -> float:
        if len(self.heap1) == (len(self.heap2)):
            x = self.heap1[0] + -self.heap2[0]
            return x/2
        else:
            return -self.heap2[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()