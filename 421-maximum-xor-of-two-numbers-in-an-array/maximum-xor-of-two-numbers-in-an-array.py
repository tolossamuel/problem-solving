class Trie:
    def __init__(self):
        self.children = [None,None]
        
class Solution:
    def __init__(self):
        self.root = Trie()
    def findMaximumXOR(self, nums: List[int]) -> int:
        ma = max(nums)
        
        bitlength = ma.bit_length()
        cur = self.root
        for n in nums:
            cur = self.root
            y = bin(n)
            y = y[2:]
            if len(y) < bitlength:
                t = bitlength - len(y)
                y = "0"*(t) + y
            for x in y:
                if x == "0":
                    if not cur.children[0]:
                        cur.children[0] = Trie()
                    cur = cur.children[0]
                else:
                    if not cur.children[1]:
                        cur.children[1] = Trie()
                    cur = cur.children[1]
            
        cur = self.root
        _min = min(nums)
        _max = 0
        if _min == 0:
            _max = ma
        for n in nums:
            if n == 0:
                continue
            cur = self.root
            t = pow(2,bitlength)-1
            mul = pow(2,bitlength-1)
            
            m = n
            y = bin(n)
            y = y[2:]
            if len(y) < bitlength:
                tt = bitlength - len(y)
                y = "0"*(tt) + y
            for x in y:
                if x == "0":
                    if not cur.children[1] and not cur.children[0]:
                        _max = max(_max,t^m)
                        print(t,m,"==")
                        break
                    elif not cur.children[1]:
                        cur = cur.children[0]
                        t -= mul
                    else:
                        cur = cur.children[1]
                else:
                    if (not cur.children[1] and not cur.children[0]):
                        _max = max(_max,t^m)
                        break
                    elif not cur.children[0]:
                        cur = cur.children[1]
                    else:
                        cur = cur.children[0]
                        t -= mul
                mul //=2 if mul > 1 else 1
       
            _max = max(_max,t^m)
        return _max

