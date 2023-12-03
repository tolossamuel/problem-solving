class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans1 = 0
        ans2 = 0
        for i in range(len(a),0,-1):
            ans1 += (int(a[i-1])*(2**((len(a)-i))))
           
        for i in range(len(b),0,-1):
            ans2 += (int(b[i-1])*(2**((len(b)-i))))
        print(ans1,ans2)
        ans1 += ans2
        ans2 = ""
        if ans1==0:
            return "0"
        print(ans1)
        while(ans1 >0):
            ans2 = str(ans1%2)+ans2
            ans1 //= 2
        
        return ans2

