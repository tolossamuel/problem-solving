class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        dp = []
        for i in range(m):
            temp = []
            for y in range(n):
                temp.append([0,0])
            dp.append(temp)

        for x,y in guards:
            
            dp[x][y] = [1,1]
        for x,y in walls:
            dp[x][y] = [-1,-1]

        for i in range(m):
            for y in range(n):
                if i==0:
                    if y != 0:
                        if dp[i][y-1][1] == 1 and dp[i][y]!= [-1,-1]:
                            dp[i][y][1] = 1
                else:
                    
                    if y!= 0:
                        if dp[i][y-1][1] == 1 and dp[i][y]!= [-1,-1]:
                            
                            dp[i][y][1] = 1
                    if dp[i-1][y][0]== 1 and dp[i][y] != [-1,-1]:
                        dp[i][y][0] = 1
        for i in range(m-1,-1,-1):
            for y in range(n-1,-1,-1):
                if i == m-1:
                    if y!= n-1:
                        if dp[i][y+1][1] == 1 and dp[i][y]!= [-1,-1]:
                            dp[i][y][1] = 1
                else:
                    if y!= n-1:
                        if dp[i][y+1][1] == 1 and dp[i][y]!= [-1,-1]:
                            dp[i][y][1] = 1
                    if dp[i+1][y][0]== 1 and dp[i][y] != [-1,-1]:
                        dp[i][y][0] = 1
                    
        counter = 0
        for i in range(m):
            for y in range(n):
                if dp[i][y] == [0,0]:
                    counter +=1
        return counter