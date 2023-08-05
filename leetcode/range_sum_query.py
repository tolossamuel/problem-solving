class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        summ = 0
        for i in nums:
            summ += i
            self.prefix.append(summ)

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix[right]
        l = self.prefix[left]
        if left != 0:
            r -= self.prefix[left - 1]
        return r
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)