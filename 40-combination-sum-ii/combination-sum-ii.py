class Solution:
    def __init__(self):
        self.numbers = []
        self.check = set()
    def solve(self,values,temp,index,target,_sum):
        if _sum == target:
            x = sorted(temp)
            if tuple(x) not in self.check:
                self.check.add(tuple(x))
                self.numbers.append(x)
            return 
        if _sum > target:
            return 
        for i in range(index,len(values)):
            if i > index and values[i] == values[i-1]:
                continue
            temp.append(values[i])
            _sum += values[i]
            self.solve(values,temp,i+1,target,_sum)
            _sum -= temp.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.solve(candidates,[],0,target,0)
        return sorted(self.numbers)