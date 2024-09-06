# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def __init__(self):
            self.dic = {0: "Zero",1: "One",2: "Two",3: "Three", 4: "Four",5: "Five",6: "Six",7: "Seven",8: "Eight",9: "Nine",10: "Ten",
                11: "Eleven",12: "Twelve",13: "Thirteen",14: "Fourteen",15: "Fifteen",16: "Sixteen",17: "Seventeen",
                18: "Eighteen",19: "Nineteen",20: "Twenty",30: "Thirty",40: "Forty",50: "Fifty",60: "Sixty",
                70: "Seventy",80: "Eighty",90: "Ninety",100: "Hundred",1000: "Thousand",1000000: "Million",1000000000: "Billion"
            }
            
            self.ans = 0
    def convert(self, numbers):
        if not numbers or not numbers.isdigit():
            return "Invalid input"
        result = []
        numbers = numbers.lstrip('0')
        if len(numbers) == 3:
            result.append(self.dic[int(numbers[0])] + " Hundred")
            numbers = numbers[1:]
        numbers = numbers.lstrip('0')
        if len(numbers) == 2:
            if int(numbers) in self.dic:
                result.append(self.dic[int(numbers)])
            else:
                result.extend([self.dic[int(numbers[0])*10], self.dic[int(numbers[1])]])
        numbers = numbers.lstrip('0')
        if len(numbers) == 1:
            result.append(self.dic[int(numbers[0])])
        return " ".join(result)

    def numberToWords(self, num: int) -> str:
        if num <= 20:
            return self.dic[num]
        pref = 1
        string = str(num)
        x = len(string)-1
        ans = ""
        while(x >= 0):
            left = x-2 if x>=2 else 0

            temp = self.convert(string[left:x+1])
            if pref == 1:
                ans = temp
                
            elif temp:
                ans  = (temp +" " + self.dic[pref] + " " + ans)
            pref *= 1000
            x -= 3
        ans = ans.strip()
        
        return ans
