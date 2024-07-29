class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_difficulty_pairs = list(zip(profit, difficulty))
        profit_difficulty_pairs.sort(key=lambda pair: pair[1])
        sorted_profit = [pair[0] for pair in profit_difficulty_pairs]
        difficulty.sort()
        _max = sorted_profit[0]
        for x in range(1,len(sorted_profit)):
            sorted_profit[x] = max(sorted_profit[x],_max)
            _max = max(sorted_profit[x],_max)
      

      
        _sum = 0
        for x in worker:
            index = bisect.bisect_right(difficulty,x)
            if index == 0:
                continue
            index -= 1
            _sum += sorted_profit[index]

        return _sum