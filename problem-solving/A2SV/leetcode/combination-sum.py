class Solution:

    def __init__(self):
        self.ans = []
    def travel(self,node,target,temp,_sum,start):
        if _sum == target:
            self.ans.append(list(temp))
        if _sum > target:
            return
        for i in range(start,len(node)):
            _sum += node[i]
            temp.append(node[i])
            self.travel(node,target,temp,_sum,i)
            temp.pop()
            _sum -= node[i]
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.travel(candidates,target,[],0,0)
        # print(self.ans)
        return self.ans
