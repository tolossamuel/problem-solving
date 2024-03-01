class Solution:
    def __init__(self):
        self.dic = {
            "2" : "abc","3" : "def","4" : "ghi","5" : "jkl",
            "6" : "mno","7" : "pqrs","8" : "tuv","9" : "wxyz"
        }
        self.ans = []
    def travel(self,node,pas):
        if not node:
            return        
        key = node[-1]
        letter = self.dic[key]
        temp = []
        for i in range(len(letter)):
            
            for y in range(len(pas)):
                temp.append(letter[i] + pas[y])
        pas = temp
        self.ans = pas.copy()
        self.travel(node[:-1],pas)
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return list(self.dic[digits[0]])
        self.travel(digits[:-1],list(self.dic[digits[-1]]))
        return self.ans