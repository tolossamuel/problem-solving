class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        dir = 1
        x = 0
        y = 0
        ans = []
        while(True):
            
            if dir == 1:
                ans.append(mat[x][y])

                if x-1>= 0 and y+1<len(mat[0]):
                    x-= 1
                    y += 1
                elif y+1 < len(mat[0]):
                    y += 1
                    dir = 0
                elif x+1 < len(mat):
                    x += 1
                    dir = 0
                else:
                    break
            elif dir == 0:
                ans.append(mat[x][y])
               
                if x+1 < len(mat) and y-1 >=0:
                   
                    x+=1
                    y -= 1
                    

                elif x+1 < len(mat):
                    x += 1
                    dir = 1
                elif y+1 < len(mat[0]):
                    y += 1
                    dir = 1
                    
                else:
                    break
           
              
        return ans