class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        x = 0
        y = 0
        ans = []
        while(x < len(firstList) and y < len(secondList)):
            if x < y:
                if firstList[x][1] == secondList[y][0]:
                    ans.append([secondList[y][0],secondList[y][0]])
                    x+=1
            elif y < x:
                if firstList[x][0] == secondList[y][1]:
                    ans.append([secondList[y][1],secondList[y][1]])
                    y+=1
            if x >= len(firstList) or y >= len(secondList):
                break
            if firstList[x][0] <= secondList[y][1] and secondList[y][0] <= firstList[x][1]:
                ans.append([max(firstList[x][0],secondList[y][0]),min(firstList[x][1],secondList[y][1])])
            if firstList[x][1] > secondList[y][1]:
                y+=1
            else:
                x += 1
            
   
        return ans