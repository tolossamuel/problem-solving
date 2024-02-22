class RecentCounter:

    def __init__(self):
        self.dif = deque()

    def ping(self, t: int) -> int:
        self.dif.append(t)
        while(self.dif[0] < (t-3000)):
            self.dif.popleft()
        return len(self.dif)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)