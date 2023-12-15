class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        checker = True
        start = paths[0][0]
        while(checker):
            checker = False
            for i in range(len(paths)):
                if start == paths[i][0]:
                    start = paths[i][1]
                    checker = True
        return start