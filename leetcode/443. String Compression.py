class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars)== 1:
            return 1
        if not chars:
            return 0
        # left = 0
        counter = 1
        result = []
        result.append(chars[0])
        for i in range(1,len(chars),+1):
            if chars[i] == result[-1]:
                counter += 1
            else:
                if counter > 1:
                   
                    letter = str(counter)
                    letter = list(letter)
                    # print(letter)
                    result += letter
                   
                    counter = 1
                    
                result.append(chars[i])
        if counter > 1:
            letter = str(counter)
            letter = list(letter)
            # print(letter)
            result += letter
            
            counter = 1
        for i in range(len(chars)- len(result)):
            chars.pop()
        for i in range(len(chars)):
            if chars[i]!= result[i]:
                chars.pop(i)
                chars.insert(i,result[i])
      
        # print(chars)
        return len(result)

        