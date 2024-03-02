class Solution:
    def __init__(self):
        self.visited = set()
        self.cells = []
        self.letter =""
    def dfs(self,letter,x,y):
        if not letter:
            return True
        if x < 0 or x >= len(self.cells) or y < 0 or y >= len(self.cells[0]):
            return 
        if (x, y) in self.visited or self.cells[x][y] != letter[0]:
            return False
        
        self.visited.add((x, y))
        result = (
            self.dfs(letter[1:], x + 1, y) or
            self.dfs(letter[1:], x - 1, y) or
            self.dfs(letter[1:], x, y + 1) or
            self.dfs(letter[1:], x, y - 1)
        )
        self.visited.remove((x, y))
        return result
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.cells = board.copy()
        self.letter = word
        for i in range(len(board)):
            for y in range(len(board[0])):
                if board[i][y] == word[0]:
                    if self.dfs(word,i,y):
                       
                        return True

        return False