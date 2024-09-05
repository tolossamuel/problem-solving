class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        arr = []
        counter = 1
        for i in range(1,len(prices)):
            if prices[i]+1 == prices[i-1]:
                counter += 1
            else:
                arr.append(counter)
                counter = 1
        arr.append(counter)
        _sum = 0
        for x in arr:
            _sum += sum(range(x+1))
        return _sum