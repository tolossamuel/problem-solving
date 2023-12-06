
class Solution:    
    def countX(self,L,R,X):
        #code here
        ans = 0
        for i in range(L+1,R):
            ans += str(i).count(str(X))
        return ans
