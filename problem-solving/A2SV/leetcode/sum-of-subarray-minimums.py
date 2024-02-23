class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        stack.append([arr[0],0])
        ans = 0
        for i in range(1,len(arr)):
            while stack and stack[-1][0] >= arr[i] :
                x = stack.pop()
                right = i - x[1]
                left = x[1] - stack[-1][1] if stack else x[1]+1
                ans += (x[0]*left*right)
                # print(ans,left,right)
            
            stack.append([arr[i],i])
        
        # print(ans)
        while(stack):
            x = stack.pop()
            right = len(arr) - x[1]
            left = x[1] - stack[-1][1] if stack else x[1]+1
            ans += (x[0]*left*right)
            
        # print(ans)
                
        return ans%mod