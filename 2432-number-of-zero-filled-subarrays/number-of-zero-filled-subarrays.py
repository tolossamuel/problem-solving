class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        counter = 0
        arr = []
        for x in nums:
            if x != 0:
                arr.append(counter)
                counter = 0
            else:
                counter += 1
        arr.append(counter)
        _sum = 0
        for x in arr:
            _sum += sum(range(x+1))
        return _sum
