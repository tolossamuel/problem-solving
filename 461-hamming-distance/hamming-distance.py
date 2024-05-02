class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0

        while(x > 0 or y > 0):
            if not((x&1) == (y&1)):
                counter += 1
            x >>= 1
            y >>= 1
        return counter