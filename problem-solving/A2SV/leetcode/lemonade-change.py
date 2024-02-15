class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0,10:0}
        dic[0]  = len(bills)
        _sum = 0
        for i in range(len(bills)):
            if bills[i] == 10:
                if dic[5] >=1:
                    dic[5] -= 1
                    dic[10] += 1
                else:
                    # print(123)
                    return False
            elif bills[i] == 20:
                if (dic[10] >= 1 and dic[5] >= 1):
                    dic[10] -= 1
                    dic[5] -= 1
                elif dic[5] >= 3:
                    dic[5] -= 3
                else:
                    # print(123)
                    return False
            else:
                dic[5] += 1   

                
                    
        return True



        