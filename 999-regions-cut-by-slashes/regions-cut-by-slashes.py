class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        matrix = [[0 for _ in range(len(grid[0]*3))] for _ in range(len(grid)*3)]
        def mark(x,y,direction):
            nonlocal matrix
            if direction == 'l':
                for i in range(3): 
                    matrix[x+i][y-i] = 1
            else:
                for i in range(3):
                    matrix[x+i][y+i] = 1
        for i in range(len(grid)):
            row = 3*i
            y = 0
            index = 0
            while(y < len(matrix[row])):
                if index >= len(grid):
                    break
                if grid[i][index] == ' ':
                    y += 3 
                    index += 1
                elif grid[i][index] == '\\':
                    mark(row,y,'r')
                    y += 3
                    index += 1
                else:
                    y += 2
                    mark(row,y,'l')
                    y += 1
                    index += 1
        counter =0 
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def check(x,y):
            nonlocal matrix
            if (0<= x  < len(matrix) and 0 <= y < len(matrix)):
                return True
            return False
        def dfs(x,y):
            nonlocal matrix
            matrix[x][y] = 1
            for i,j in dir:
                new_x = x + i
                new_y = y + j
                if check(new_x,new_y) and matrix[new_x][new_y] == 0:
                    dfs(new_x,new_y)
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                if matrix[x][y] == 0:
                    counter += 1
                    dfs(x,y)
        return counter

            
