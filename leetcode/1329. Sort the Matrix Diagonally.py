class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        for i in range(len(mat)-1,0,-1):
            col = 0
            row = i-1
            pos_y = 0
            pos_x = i -1
            y = min((len(mat)-i),(len(mat[i])))+1

            for z in range(y-1):
               
                for x in range(y-1):
                    row += 1
                    col += 1
                    try:
                        if mat[pos_x][pos_y] > mat[row][col]:
                           
                            
                            mat[pos_x][pos_y], mat[row][col] = mat[row][col], mat[pos_x][pos_y]
                             

                    except:
                        pass
                    
                  
                pos_x += 1
                pos_y += 1
                row = pos_x
                col = pos_y
        for i in range(len(mat[0])-1,0,-1):
            col = i - 1
            row = 0
            pos_y = i - 1
            pos_x = 0
            y = min((len(mat[0])-i),(len(mat)))+1
            
            for z in range(y-1):
               
                for x in range(y-1):
                    row += 1
                    col += 1
                    try:
                        if mat[pos_x][pos_y] > mat[row][col]:
                           
                            
                            mat[pos_x][pos_y], mat[row][col] = mat[row][col], mat[pos_x][pos_y]
                             

                    except:
                        pass
                    
                  
                pos_x += 1
                pos_y += 1
                row = pos_x
                col = pos_y

        return mat
      
