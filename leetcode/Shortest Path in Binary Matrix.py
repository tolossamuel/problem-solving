
def shortestPathBinaryMatrix( grid):
        global list1
        list1 =  []
        global temp
        temp = []
        if grid[0][0] != 0:
            return (-1)
        def dfs(x,y):
            global list1
            global temp
            print(temp)
            print(list1,"list")
            if grid[x][y]==1:
                temp.pop()
                return 
            if grid[x][y] <= 6:
                 grid[x][y] +=2
            else:
                 grid[x][y] = 1
            if y+1 == len(grid[0]) and x+1 == len(grid):
                if temp:
                    print(x+1,y+1 ,"yess")
                    temp.append([x,y])
                    list1.append(temp)
                    print(list1,"iffff")
                temp = []
                return 
            if x+1 <(len(grid)):
                temp.append([x,y])
                
                dfs(x+1,y)
            if y+1 <(len(grid[0])):
                temp.append([x,y])
                dfs(x,y+1)
            if x-1 >=0 and grid[x-1][y] == 0:
                temp.append([x,y])
                dfs(x-1,y)
            if y-1 >=0:
                temp.append([x,y])
                dfs(x,y-1)
            if y+1 <(len(grid[0])) and x+1 <(len(grid)):
                temp.append([x,y])
                dfs(x+1,y+1)
            if y+1 <(len(grid[0])) and x-1 >= 0:
                temp.append([x,y])
                dfs(x-1,y+1)
            if x+1 <len(grid) and y-1 >= 0:
                temp.append([x,y])
                dfs(x+1,y-1)
            if y-1 >=0 and x-1 >= 0:
                temp.append([x,y])
                dfs(x-1,y-1)
            
        print(list1)
        dfs(0,0)
        small = -1
        print("=======================================================")
        if list1:
            small = len(list1[0])
        for i in range(len(list1)):
                print(small, len(list1[i]))
                if small > len(list1[i]):
                    small = len(list1[i])
                    print(list1[i])
        return small
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix( grid))
