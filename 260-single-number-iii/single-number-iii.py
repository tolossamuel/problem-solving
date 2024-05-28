class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        one = 0
        two = 0
        mask = xor & -xor
        for x in nums:
            if mask & x:
                one ^= x
            else:
                two ^= x
        return [one,two]

