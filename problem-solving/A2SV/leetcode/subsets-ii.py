class Solution:
    def __init__(self):
        self.ans = [[]]
        self.dic = {}
    def helper(self,arr,size,val):
        if val >= len(arr):
            return 
        for i in range(size):
            if self.ans[i] == [] and (arr[val]) not in self.dic:
                self.ans.append([arr[val]])
                self.dic[arr[val]] = 1
            elif self.ans[i] != [] and (tuple(self.ans[i] + [arr[val]]) not in self.dic):
                self.ans.append(self.ans[i] + [arr[val]])
                key = tuple(self.ans[i] + [arr[val]])
                self.dic[key] = 1
        return self.helper(arr,len(self.ans),val+1)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.helper(nums,1,0)
        # print(self.ans)
        return self.ans