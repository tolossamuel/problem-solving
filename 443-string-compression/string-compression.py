class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""
    
        values = []
        if len(chars) == 1:
            return 1
        if not chars:
            return 0
        values.append(chars[0])
        newAns = 0
        
        for i in range(1,len(chars)):
            if chars[i] != values[-1]:
                if len(values) > 1:
                    
                    s+= values[-1]
                    s += str(len(values))
                else:
                    
                    s += values[-1]
                values = []
                values.append(chars[i])
            else:
                values.append(chars[i])
               
        else:
            if len(values) > 1:
                    
                    s+= values[-1]
                    s += str(len(values))
            else:
                s += values[-1]
        s = list(s)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)