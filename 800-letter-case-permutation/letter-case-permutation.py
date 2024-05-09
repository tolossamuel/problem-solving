class Solution:
    def travel(self,start,word): 
        self.temp.append(word)
        for i in range(start,len(self.s)):
            if self.s[i].isalpha():
                self.travel(i+1,self.s[i])
                self.travel(i+1,self.s[i].swapcase())
            else:
                self.travel(i+1,self.s[i])
        if (len(self.temp)-1) == len(self.s):
            self.ans.append("".join(self.temp))
        self.temp.pop()
        return 
        
    def letterCasePermutation(self, s: str) -> List[str]:
        self.ans = []
        self.s = s
        self.temp = []
        self.travel(0,"")
        return self.ans