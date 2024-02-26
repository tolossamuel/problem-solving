class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack1 = []
        stack2 = []
        stack3 = []
        ans = []
        n = 0
        left = 0
        for i in range(len(s)):
            if s[i].isdigit():
                n*= 10
                n += int(s[i])
            elif s[i] =='[':
                stack2.append(len(stack3))
                stack1.append(n)
                n = 0
            elif s[i] ==']':
               
                stack3 += ((stack1[-1]-1) *stack3[stack2[-1]:len(stack3)])
                stack2.pop()
                stack1.pop()
                n = 0
            else:
                stack3.append(s[i])
        
        stack3 = "".join(stack3)
        return stack3
            
        