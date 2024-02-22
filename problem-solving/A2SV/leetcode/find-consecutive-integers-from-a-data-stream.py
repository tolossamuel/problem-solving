class DataStream:

    def __init__(self, value: int, k: int):
        self.dic = deque()
        self.val = value
        self.k = k
    def consec(self, num: int) -> bool:
        if num != self.val:
            self.dic = deque()
            return False
        self.dic.append(num)
        if len(self.dic) == self.k:
            self.dic.pop()
            return True
        return False



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)