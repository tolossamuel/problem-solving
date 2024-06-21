class Solution:
    def reverseBits(self, n: int) -> int:
        mul = 1
        total = 0
        n = bin(n)[2:]
        n = "0" *(32 - len(n)) + n
        for i in n:
            if i == "1":
                total += mul
            mul *= 2
        return total