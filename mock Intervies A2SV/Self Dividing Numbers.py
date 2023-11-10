class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numberList = []
        def supporter( num):
            string = str(num)
            for i in string:
                if int(i) == 0:
                    return False
                elif num %  int(i)!= 0:
                    return False
            return True
        for i in range(left,right+1,+1):
            if (supporter(i)):
                numberList.append(i)
        return numberList