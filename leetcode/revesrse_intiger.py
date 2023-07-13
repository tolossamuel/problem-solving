class Solution:
    def reverse(self, x: int) -> int:
        b=0
        x=list(str(x))
        if(x[0]=='-'):
            b=1
            x.remove('-')
        x.reverse()
        x="".join(x)
        x=int(x)
        if(b==1):
            x*=-1
        if(x>=(2**31) or x<(-2**31)):
            return 0
        return x