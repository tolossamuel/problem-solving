class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        x = self.dic[key]
        index = bisect.bisect_left(x,[timestamp,""])
        left = 0
        right = 0
        if not x:
            return ""
        if index >= len(x):
            return x[-1][1]
        elif timestamp ==  x[index][0]:
            return x[index][1]
        elif index == 0:
            return ""
        else:
            return x[index - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)