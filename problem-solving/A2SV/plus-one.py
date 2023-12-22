class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b=""
        for i in range(len(digits)):
            b+=str(digits[i])
        b=int(b)+1
        b=str(b)
        digits.clear()
        for i in range(len(b)):
            digits.append(int(b[i]))
        return digits