class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumOf = 0
        product = 1
        while(n):
            sumOf += (n%10)
            product *= (n%10)
            n //= 10
        return product - sumOf