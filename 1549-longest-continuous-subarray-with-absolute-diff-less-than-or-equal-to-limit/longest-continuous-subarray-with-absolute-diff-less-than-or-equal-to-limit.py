class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        _min = deque()
        _max = deque()
        _min.append(nums[0])
        _max.append(nums[0])
        x = 0
        i = 1
        ans = 1
        while(i < len(nums)):
            while(_min and _min[-1] > nums[i]):
                _min.pop()
            
            while(_max and _max[-1] < nums[i]):
                _max.pop()
            _max.append(nums[i])
            _min.append(nums[i])
            while(x < i):
                if abs(_min[0] - _max[0]) <= limit:
                    ans = max(ans,(i-x+1))
                    break
                else:
                
                    if _min[0] == nums[x]:
                        _min.popleft()
                    if _max[0] == nums[x]:
                        _max.popleft()
                    x += 1
            i += 1
        return ans
