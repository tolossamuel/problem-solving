class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def check(x,y):
            if 0 <= x < len(dungeon) and 0 <= y < len(dungeon[0]):
                return True
            return False
        n = len(dungeon)
        m = len(dungeon[0])
        arr = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            for y in range(m-1,-1,-1):
                if i == n-1 and y == m-1:
                    arr[i][y] = -dungeon[i][y]
                    if dungeon[i][y] > 0:
                        arr[i][y] = 0
                    continue
                left = float("inf")
                right  = float("inf")
                if check(i+1,y):
                    left = arr[i+1][y]
                if check(i,y+1):
                    right = arr[i][y+1]
                if left <= right:
                    dungeon[i][y] -= left
                    arr[i][y] = -dungeon[i][y]
                    if dungeon[i][y] >= 0:
                        dungeon[i][y] = 0
                        arr[i][y] = 0
                else:
                    dungeon[i][y] -= right
                    arr[i][y] = -dungeon[i][y]
                    if dungeon[i][y] >= 0:
                        dungeon[i][y] = 0
                        arr[i][y] = 0
        return arr[0][0] + 1




            
        return ans