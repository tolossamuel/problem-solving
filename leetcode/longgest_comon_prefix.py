class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        b=[]
        c=0
        for y in range(len(strs[0])):
            try:
                for i in range(len(strs)):
                    if(strs[0][y] == strs[i][y]):
                        c+=1
                if(c==len(strs)):
                    b.append(strs[0][y])
                else:
                    b="".join(b)
                    return b
                c=0
                
            except:
                pass
        b="".join(b)
        return b
        