class Solution:
    def __init__(self):
        self.ans = []
    def permutations(self,arr,start):
        if start == len(arr):
            self.ans.append(list(arr))
        for i in range(start,len(arr)):
            arr[i],arr[start] = arr[start],arr[i]
            self.permutations(arr,start + 1)
            arr[i],arr[start] = arr[start],arr[i]
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations(nums,0)
        return self.ans