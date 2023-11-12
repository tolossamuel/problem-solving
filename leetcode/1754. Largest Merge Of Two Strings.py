class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        merge = ""
        
        if word1:
            merge += word1[0]
            if not word2:
                merge = word1
                return merge
        elif( wrod2) :
            merge = word2
            return merge
        
        elif (not word1 and not word2):
            return ""
        left  = 0
        n,m = len(word1), len(word2)
        right = 0
        merge = ""
        while (left < n) and (right < m):
            if (word1[left]> word2[right]):
                merge += word1[left]
                left += 1
            elif (word2[right] > word1[left]):
                merge += word2[right]
                right += 1
            else:
                if (word1[left:]> word2[right:]):
                    merge += word1[left]
                    left += 1
                else:
                    merge += word2[right]
                    right += 1
        merge += (word1[left:]+word2[right:])
        return merge
        
                