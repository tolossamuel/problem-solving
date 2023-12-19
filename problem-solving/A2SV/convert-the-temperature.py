class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        digree = []
        digree.append(celsius+273.15)
        digree.append( (celsius * 1.80 + 32.00))
        return digree
        