class Solution:
   
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counter = 0
        ans = defaultdict(int)
        def helper(index):
            nonlocal counter
            nonlocal ans
            if index >= len(nums):
                if ans:
                    counter += 1
                return 
            if nums[index]+k not in ans and nums[index]-k not in ans:
                ans[nums[index]] += 1
                helper(index+1)
                ans[nums[index]] -= 1
                if ans[nums[index]] == 0:
                    ans.pop(nums[index])
                helper(index+1)
            else:
                helper(index+1)
        helper(0)
        return counter