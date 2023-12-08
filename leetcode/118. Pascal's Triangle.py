class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        result = [[1]]
        global temp
        temp = []
        def pascal(arr,index):
            global temp
            if len(result) == numRows:
                return
            else:
                if index == 0:
                    temp.append(arr[index])
                
                    
                    
                if index == (len(arr)-1):
                    
                    temp.append(arr[index])
                    result.append(list(temp))
                    
                    
                    temp = []
                    pascal(result[-1],0)
                else:
                    
                    temp.append(arr[index]+arr[index+1])
                    
                    pascal(arr,index+1)
        pascal([1],0)
        print(result)
        return result

