class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x
        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self,x,y):
        # print(x,y)
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp: return 
        if self.size[xp] > self.size[yp]:
            self.size[xp] += self.size[yp]
            self.dic[yp] = xp
            self.sum[xp] += self.sum[yp]
            
        else:
            self.size[yp] += self.size[yp]
            self.dic[xp] = yp
            self.sum[yp] += self.sum[xp]
    def findMx(self):
        return max(self.sum.values())
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        self.dic = {x:x for x in range(len(nums))}
        self.size = {x:1 for x in range(len(nums))}
        self.sum = defaultdict(int)
        ans = []
        check = [0]*len(nums)
        _max = float("-inf")
        for x in range(len(removeQueries)-1,-1,-1):
            check[removeQueries[x]] = nums[removeQueries[x]]
            left = removeQueries[x]
            parent = self.dic[removeQueries[x]]
            self.sum[parent] += nums[removeQueries[x]]
            if self.sum[left - 1] > 0: self.union(left - 1, left)
            if self.sum[left + 1] > 0: self.union(left, left + 1)
            value = self.find(left)
            ammount = self.sum[value]
            _max = max(ammount,_max)
            ans.append(_max)
        ans.pop()
        ans.reverse()
        ans.append(0)
        return ans