class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        remider = (digits[-1] + 1)//10
        digits[-1] = (digits[-1] + 1)%10
        if remider:
            for i in range(len(digits)-2,-1,-1):
                temp = (digits[i] + remider)
                digits[i] = (temp)%10
                remider = (temp//10)
                if not remider:
                    break
            if remider == 1:
                digits.insert(0,remider)
        return digits