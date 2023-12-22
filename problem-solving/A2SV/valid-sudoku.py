class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def checkCol(arr,col,arrCol):
            if col >= len(arr):
                return True
            elif arr[col] in arrCol:
                return False
            else:
                if arr[col] != ".":
                    arrCol.append(arr[col])
                return True and checkCol(arr,col+1,arrCol)
        def checkRow(arr,col,row,arrRow):
            if row>= len(arr):
                return True
            elif arr[row][col] in arrRow:
                return False
            else:
                if arr[row][col]!= ".":
                    arrRow.append(arr[row][col])
                return True and checkRow(arr,col,row+1,arrRow)
        def checkBox(arr,col,row):
            arrCol = []
            for i in range(3):
                for y in range(3):
                    if arr[row+i][col+y] != ".":
                        if arr[row+i][col+y] in arrCol:
                            return False
                        else:
                            arrCol.append(arr[row+i][col+y])
                            print(arrCol)
            return True
            
        
        for i in range(len(board)):
            for y in range(len(board[0])):
                r = i//3
                c = y//3
                arrCol = []
                arrRow = []
                print(r*3,c*3)
                if not checkCol(board[i],0,arrCol) or not checkRow(board,y,0,arrRow) or not checkBox(board,c*3,r*3):
                    return False
        return True
            

