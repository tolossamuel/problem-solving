class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [temperatures[0]]
        stack2 = []
        ans = []
        for i in range(1,len(temperatures)):
            if temperatures[i] > stack[-1]:
                stack.append(temperatures[i])
                ans.append(1)
                while(stack2):
                    if temperatures[i] > stack2[-1][0]:
                        ans[stack2[-1][1]] = (i-stack2[-1][1])
                        stack2.pop()
                    else:
                        break
                
            else:
                stack2.append([stack[-1],i-1])
                stack = []
                ans.append(0)
                stack.append(temperatures[i])
       
        ans.append(0)
        return ans