class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dic = [[0 for i in range(len(text1)+1)] for i in range(len(text2)+1)]
        for i in range(len(text2)-1,-1,-1):
            for y in range(len(text1)-1,-1,-1):
                if text2[i] == text1[y]:
                    dic[i][y] = 1+ dic[i+1][y+1]
                else:
                    dic[i][y] = max(dic[i+1][y], dic[i][y+1])
        return dic[0][0]