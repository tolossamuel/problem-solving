class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        counter = 0
        for x in range(1, n+1):
            if n%x == 0:
                counter += 1
            if counter == k:
                return x
        return -1