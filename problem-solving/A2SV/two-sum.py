class Solution:
    b=[1,1]
    n=1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Solution.n=len(nums)
        for i in range(Solution.n-1):
            for y in range(i+1,Solution.n,+1):
                if (nums[i]+nums[y])==target:
                    Solution.b[0]=i
                    Solution.b[1]=y
                    break
                
            else:
                pass
        return Solution.b