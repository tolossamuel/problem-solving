class Solution:
    def __init__(self):
        self.arr = [1]
    def helper(self,rowIndex:int):
        if rowIndex == 0:
            return 0
        help = [1]
        for i in range(len(self.arr)-1):
            help.append(self.arr[i+1] + self.arr[i])
        help.append(1)
        self.arr = help
        self.helper(rowIndex-1)
    def getRow(self, rowIndex: int) -> List[int]:
       
            if rowIndex == 0:
                return [1]
            self.helper(rowIndex)
            print(self.arr)
            return self.arr
            