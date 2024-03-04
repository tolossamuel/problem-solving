class Solution:
    def __init__(self):
        self.numbers = []
    def solve(self,k,n,temp,_sum,index):
        if _sum == n and k == 0:
            self.numbers.append(list(temp))
            return 
        if k == 0:
            return
        for i in range(index,10):
            temp.append(i)
            k -= 1
            _sum += i
            self.solve(k,n,temp,_sum,i+1)
            k += 1
            _sum -= temp.pop()
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.solve(k,n,[],0,1)
        return self.numbers