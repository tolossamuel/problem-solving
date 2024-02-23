class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        stack = [nums[0]]
        _min = [stack[0],0]
        _max = [stack[0],0]
        ans = 1
        for i in range(1,len(nums)):
            stack.append(nums[i])
            if stack:
                if _min[0] >= nums[i]:
                    _min = [nums[i],len(stack)-1]
                if _max[0] <= nums[i]:
                    _max = [nums[i],len(stack)-1]
                x = abs(_min[0] - _max[0])
            
                if x <= limit:
                    ans = max(ans,len(stack))
                else:
                    while(stack):
                       
                        size = min(_min[1],_max[1])
                        stack = stack[size+1:]
                        x = min(stack)
                        index = stack.index(x)
                        _min = [x,index]
                        x = max(stack)
                        index = stack.index(x)
                        _max = [x,index]
                        x = abs(_min[0] - _max[0])
                        if x <= limit:
                            ans = max(ans,len(stack))
                            break
        
        return ans

    