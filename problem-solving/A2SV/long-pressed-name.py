from collections import Counter
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
        x = 0
        y = 0
        countElementTyped =0
        countElementName =0
        storCountTyped = 0
        numOfDiff = 0
        while(x < len(name) and y < len(typed)):
            if name[x] == typed[y]:
                numOfDiff = 0
                countElementName =0
                countElementTyped += 1
                y += 1
            else:
                numOfDiff += 1 if name[x] != typed[y-1] else 0
                if numOfDiff==1:
                    return False 
                storCountTyped = countElementTyped if countElementTyped > 0 else storCountTyped
                countElementTyped = 0
               
                x += 1
                countElementName+=1


            if countElementName > storCountTyped or (x >=  len(name) and y < len(typed)):
                return False
            if y >= len(typed) and len(set(name[x:])) >1:
                return False
        return True

