class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        def solve(a,b):
            l = 0
            r = 0
            s = []
            n = len(a)
            m = len(b)
            while(l < len(a) and r < len(b)):
                s += a[l:l+2]
                if n <= m:
                    s += b[r:r+2]
                    r += 2
                    m -= 2
                else:
                    s += b[r]
                    r += 1
                    m -= 1
                l += 2
                n -= 2
                
            
            s += b[r:]
            s += a[l:]

            s = "".join(s)

            return s
        if (a < b):
            return solve('b'*b,'a'*a)
        
        return solve('a'*a,'b'*b)