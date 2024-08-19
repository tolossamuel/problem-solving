class Solution:
    def minSteps(self, n: int) -> int:
        current = 0
        operation = 0
        size = 1
        n -= 1
        while(n > 0):
            if (n%size == 0):
                current  = size
                n -= size
                size += size
                operation += 2
            else:
                operation += 1
                size += current
                n -= current
            
        return operation
