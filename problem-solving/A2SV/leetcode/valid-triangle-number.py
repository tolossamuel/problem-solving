class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        for i in range(2,len(nums)):
            for y in range(i):
                x = nums[i] - nums[y] + 1
                pos = bisect.bisect_left(nums,x)
                if pos >= y:
                    continue
                else:
                    counter += (y-pos)
        return counter
