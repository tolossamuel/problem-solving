class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}
        def solve(index,visited):
            if index >= len(nums1):
                return 0
            if (index,visited) in cache:
                return cache[(index,visited)]
            min_ans = float("inf")

            for i in range(len(nums2)):
                if (visited & (1 << i)) == 0:
                    visited ^= (1<<i)
                    min_ans = min(
                        min_ans,
                        solve(index+1,visited) + ( nums1[index]^nums2[i])
                        
                    )



                    
                    visited ^= (1<<i)
            cache[(index,visited)] = min_ans
            return min_ans
        ans = solve(0,0)
        return ans if ans != float("inf") else 1