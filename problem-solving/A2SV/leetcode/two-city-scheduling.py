class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        x = sorted(costs,key = lambda x: x[0] - x[1])
        counter = 0
        for i in range(len(costs)//2):
            counter += x[i][0]
        for i in range(len(costs)//2,len(costs)):
            counter += x[i][1]
        return counter