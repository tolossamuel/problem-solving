class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        for i in range(n+1):
            counter = 0
            while(i > 0):
                if i%2 == 1:
                    counter += 1
                i //= 2
            arr.append(counter)
        return arr
        