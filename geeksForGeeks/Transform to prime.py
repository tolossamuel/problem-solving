class Solution:
    def minNumber(self, arr,n):
        # code here
        sumOf = sum(arr)
        if sumOf <=2:
            return (2-sumOf)
        elif sumOf <=3:
            return (3-sumOf)
        elif sumOf <=5:
            return (5-sumOf)
        elif sumOf <=7:
            return (7-sumOf)
        elif sumOf <= 11:
            return (11-sumOf)
        
            
        while(True):
            
            m = int(sumOf**0.5)
            for i in range(2,(m+1)):
                if sumOf%i == 0:
                    break
            else:
               
                return (sumOf - sum(arr))
            
            sumOf +=1