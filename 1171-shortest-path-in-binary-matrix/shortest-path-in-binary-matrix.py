class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        def check(x,y):
            if (0<= x < len(grid) and 0 <= y < len(grid[0])):
                return True
            return False
        def travel(stack):
            level = 1
            visited = set([(0,0)])
            dir = [(1,0),(0,1),(1,1),(1,-1),(0,-1),(-1,-1),(-1,1),(-1,0)]
            while(stack):
                n = len(stack)
          
                for i in range(n):
                    curr = stack.popleft()
                    if curr[0] == (len(grid)-1) and curr[1] == (len(grid[0])-1):
                        return level
                    for x,y in dir:
                        if check(curr[0]+x,curr[1]+y) and (curr[0]+x,curr[1]+y) not in visited and grid[curr[0]+x][curr[1]+y] == 0:
                                visited.add((curr[0]+x,curr[1] + y))
                                stack.append([curr[0]+x,curr[1]+y])
                level += 1
            return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        return travel(deque([[0,0]]))