class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newWord = ""
        for i in range(max(len(word1),len(word2))):
            
            if (len(word1)>i):
                newWord += word1[i]
            if (len(word2)>i):
                newWord += word2[i]
        return newWord