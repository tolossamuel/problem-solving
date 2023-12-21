class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        x = 10e4
        for i in range(len(ghosts)):
            y = abs(ghosts[i][0] - target[0]) + abs(ghosts[i][1] - target[1])
            x = min(x,(y))
        p = (abs(target[0]) + abs(target[1]))
        print(x,p)
        if x > p:
            return True
        return False