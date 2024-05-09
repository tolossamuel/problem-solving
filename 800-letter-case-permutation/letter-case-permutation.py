class Solution:
    def travel(self,start,word): 
        for i in range(start,len(self.s)):
            if self.s[i].isalpha():
                self.travel(i+1,word + self.s[i].upper())
                self.travel(i+1,word+ self.s[i].lower())
            else:
                self.travel(i+1,word+self.s[i])
        if len(word) == len(self.s):
            self.ans.append(word)
        return 
        
    def letterCasePermutation(self, s: str) -> List[str]:
        self.ans = []
        self.s = s
        self.travel(0,"")
        return self.ans