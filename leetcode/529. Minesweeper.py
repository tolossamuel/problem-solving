class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])

        def get_neighbours(i,j):
            neighbours = []
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == dj == 0:
                        continue

                    ip, jp = i + di, j + dj
                    if 0<= ip < m and 0 <= jp < n:
                        neighbours.append((ip, jp))
            return neighbours

        def expand(i, j, board):
            neighbours = get_neighbours(i,j)

            num_mines = 0
            for ip, jp in neighbours:
                if board[ip][jp] == 'M':
                    num_mines += 1

            if num_mines:
                board[i][j] = str(num_mines)
            else: 
                board[i][j] = 'B'
                for ip, jp in neighbours:
                    if board[ip][jp] == 'E':
                        board = expand(ip, jp, board)
            return board

        i, j = click

        clicked = board[i][j]

        if clicked == 'M':
            board[i][j] = 'X'
        elif clicked == 'E':
            board = expand(i, j, board)

        return board
        