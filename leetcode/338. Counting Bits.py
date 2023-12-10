class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
       
        for i in range(n+1):
            sum = bin(i).count("1")
            print(bin(i))
            result.append(sum)
        return result