class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        temp = []
        def helper(index):
            if index >= len(nums):
                if temp:
                    ans.append(temp.copy())
                return 
            temp.append(nums[index])
            helper(index+1)
            temp.pop()
            helper(index+1)
        helper(0)
        return ans
