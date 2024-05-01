class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            num = i
            bit_counter = 0
            while(num > 0):
                if num & 1:
                    bit_counter += 1
      
                num >>= 1
            if bit_counter == k:
                ans += nums[i]
        return ans
