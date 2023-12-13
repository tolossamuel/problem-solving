class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def permutations(n,x):
            if n == 0:
                return x
            if n == 1:
                return x
            else:
                x *= n
                return permutations(n-1,x)
        totalMove = permutations(m+n-2,1)
        totalChoise = permutations(m-1,1)
        totalCount = permutations(n-1,1)
        return (totalMove/(totalChoise*totalCount))
