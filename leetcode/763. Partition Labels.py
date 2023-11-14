class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if len(s) == 1:
            return [1]
        if not s:
            return [0]
        left = 0
        current = 0
        checker = False
        value = []
        n = len(s)
        index = 0
        for i in range(n):
            left  = i
            while(left < n):
                if s[i] == s[left]:
                    checker = True
                    current = left+1
                

                left += 1
            
     
            if (i == index) and index > 0:
                if value:
                    value.append(index - sum(value))
                else:
                    value.append(index)
                index = 0
            if checker:
                index = max(current, index)
        if index != 0:
            if value:
                value.append(index - sum(value))
                print(index)
            else:
                value.append(index)
                print(index)
            
                
                
                    
        return value


