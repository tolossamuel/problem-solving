class Solution:
    def __init__(self):
        self.ans = []
    def combinations(self,start,limit,size,temp):
        if limit == 0:
            print(temp)
            self.ans.append(list(temp))
            if temp:
                temp.pop()
            return 
        for i in range(start,size+1):
            temp.append(i)
            # print(temp,limit)
            self.combinations(i + 1,limit - 1,size,temp)
        if temp:
            temp.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations(1,k,n,[])
        # print(self.ans)
    
        return self.ans