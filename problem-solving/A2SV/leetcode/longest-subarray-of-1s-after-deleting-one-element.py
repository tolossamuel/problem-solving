class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        index = 0
        ans = 0
      
        for i in nums:

            if not stack:
                stack.append(i)
                
            elif i == 0:
                
                if not (i in  stack):
                    
                    stack.append(i)
                    index = len(stack)-1
                else:
                    ans = max(ans,len(stack)-1)
                    print(stack,index)
                    stack = stack[index+1:len(stack)]
                    
                    stack.append(i)
                    index = len(stack)-1
                    # print(stack)
                    
            else:
                
                stack.append(i)
            
                
        else:
            print(stack,index)
            ans = max(ans,(len(stack)-1))
        return ans
            



            