class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
       
        
        counter = 0
        for i in words:
            
            for y in i:
              
                if i.count(y) > chars.count(y): 
                    break
            else:
                counter += len(i)
                
        return counter
                