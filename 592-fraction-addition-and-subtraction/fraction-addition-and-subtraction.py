import math
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:



        
        nums = expression.split("+")
        stack = []
        temp = ''
        divider = []
        num = ''
        for x in expression:
            if x == '-' and temp:
                if temp and temp[-1] != '/':
                     num = '1'
             
                temp += '/' + num
                    
                stack.append(temp)
                divider.append(int(num))
                num = ''
                temp = '-'
            elif x == '+' and temp:
                if temp and temp[-1]!= '/':
                    num = '1'
                
                temp += '/' + num
                    
                stack.append(temp)
         
                divider.append(int(num))
                num = ''
                temp = ''
            elif x == "-":
                temp += x
            elif x == '/':
                temp += num
                temp += '/'
                num = ''
            elif x != "+":
                num += x
            
        if not num:
            num = '1'
        if temp and temp[-1] != '/':
            temp += '/'
        if temp:
            temp += num
            stack.append(temp)
            divider.append(int(num))
        
        _lcm = math.lcm(*divider)
        _sum = 0

        for x in stack:
            num = x[0]
            temp = x.split('/')
            num = temp[0]
            neg = 1
        
            if temp[0][0] == '-':
                num = temp[0][1:]
                neg = -1
            num = int(num) * neg
            neg = 1
   
            _sum += ((_lcm//int(temp[-1])) * num)

        if(_sum) == 0:
            return '0/1'
        ans = str(Fraction(_sum,_lcm))

        if '/' not in ans:
            ans += '/1'

        return ans


# -45 + 60+ 

