class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        string = ""
        while(columnNumber>26):
            remider = columnNumber%26
            print(remider)
            
            string = letter[remider-1] + string
            columnNumber //= 26
            if remider == 0:
                columnNumber -= 1
        print(columnNumber)
        string = letter[columnNumber-1] + string
        return string
        