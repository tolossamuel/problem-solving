class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        arr = []
        common = len(A)
        visited1 = 0
        visited2 = 0
        for i in range(len(A)-1,-1,-1):
            arr.append(common)
            
            if A[i] != B[i] and (not((1 << B[i]) & visited1) and not((1<<A[i]) & visited2)):
                print(bin(visited1),bin(visited2),bin(1<<B[i]),bin(1<<A[i]), i)
                common -= 2
            elif not (((1 << B[i]) & visited1) and ((1<<A[i]) & visited2)):
                common -= 1
            visited1 |= (1<<A[i])
            visited2 |= (1<<B[i])
            
        arr.reverse()
        return arr

