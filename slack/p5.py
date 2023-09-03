board =[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
not_iceland = []
for i in board:
	print(i)
def dfs(x , y):
	if board[x][y] == "X":
		return 
	board[x][y] = 'T'

	print(x,y)
	not_iceland.append([x,y])
	direction = [(1,0),(0,1),(-1,0),(0,-1)]
	for a,b in direction:
			if (x + a)>=0 and (y + b) >=0 and (x + a) < len(board) and (y + b) < len(board):
				if board[x+a][y+b]=='O':
					dfs(x+a,y+b)
for i in range(len(board)):
	print(i)
	for y in range(len(board[0])):
		if (i == 0 or i + 1 == len(board)):
			if board[i][y] == "O":
				dfs(i, y)
		elif y > 0 and y < len(board[0])-1:
			
			print(y)
			continue
		else:
			if board[i][y] == "O":
				dfs(i, y)
for i in range(len(board)):
	for y in range(len(board[0])):
		if board[i][y] == "T":
			board[i][y] = "O"
		elif board[i][y] == "O":
			board[i][y] = "X"
			print(i,y)
		
print(not_iceland)
for i in board:
	print(i)