class Solution:
    def __init__(self):
        self.check = {1:set(),2:set()}
        self.ans = [[]]
        self.string = ""

    def solve(self,index,start,string,temp):
        if temp and temp[-1] != temp[-1][::-1]:
            temp.pop()
            return 
        if index == len(self.string):
            if not string and len("".join(temp)) == len(self.string) and len(temp) < len(self.string):
                self.ans.append(temp)
            return
        self.solve(index+1,index+1,self.string[index+1:],temp + [self.string[start:index+1]])
        self.solve(index+1,start,self.string[index+1:],temp)
    def partition(self, s: str) -> List[List[str]]:
        self.string = s
        self.ans[0] = list(s)
        self.solve(0,0,s,[])
        # print(self.ans)
        return self.ans