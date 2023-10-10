class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(len(score) -1 ):
            for y in range(i+1,len(score),+1):
                if score[i][k] < score[y][k]:
                    score[i],score[y] = score[y],score[i]
        return score
        