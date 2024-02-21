class RecentCounter:

    def __init__(self):
        self.dif = []

    def ping(self, t: int) -> int:
        self.dif.append(t)
        x = bisect.bisect_left(self.dif, (t-3000))
        return len(self.dif) - x
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)