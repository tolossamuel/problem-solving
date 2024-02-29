class Solution:
    def __init__(self):
        self.ans = [[]]
    def helper(self,arr,size,val):
        if val >= len(arr):
            return 
        for i in range(size):
            if self.ans[i] == []:
                self.ans.append([arr[val]])
            else:
                self.ans.append(self.ans[i] + [arr[val]])
        return self.helper(arr,len(self.ans),val+1)
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums,1,0)
        # print(self.ans)
        return self.ans