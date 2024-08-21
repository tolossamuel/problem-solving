class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_ = 0
        for i in nums:
            xor_ ^= i
        k = (2**maximumBit)-1
        ans = []
        for i in range(len(nums)-1,-1,-1):
            ans.append(xor_^k)
            xor_ ^= nums[i]
        return ans
