class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        _xor = 0
        for i in nums:
            _xor ^= i
        return _xor