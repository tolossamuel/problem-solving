class Solution:
    def recurtions(self,x,y,s):
        if x >= y:
            return 
        s[x],s[y] = s[y],s[x]
        self.recurtions(x+1,y-1,s)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.recurtions(0,len(s)-1,s)
        
        