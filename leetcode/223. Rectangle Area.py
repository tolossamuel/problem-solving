class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        corx = min(ax2,bx2)
        corx -= max(ax1,bx1)
        cory = min(ay2,by2)
        cory -= max(ay1,by1)
        com = 0
        print(corx,cory)
        if cory>0 and corx>0:
            com = corx*cory


        area1 = ((ax2-ax1)*(ay2-ay1))
        area2 = ((bx2-bx1)*(by2-by1))
        return (area1 + area2 -com)
