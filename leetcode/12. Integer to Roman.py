class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        string = str(num)
        result = ""
        
        sumOf = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(sumOf)):
            while num >= sumOf[i][0]:
                result += sumOf[i][1]
                num -= sumOf[i][0]
        return result