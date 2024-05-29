class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
      
        return a if b <= mask else a&mask
