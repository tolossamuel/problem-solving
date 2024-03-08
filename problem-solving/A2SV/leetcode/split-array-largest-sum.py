class Solution:
    


    def splitArray(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = sum(nums)
        def check(mid):
            _sum = 0
            size = k
            for i in range(len(nums)):
                if (_sum + nums[i]) <= mid:
                    _sum += nums[i]
                else:
                    size -= 1
                    
                    if nums[i] > mid:
                        # print(mid)
                        _sum = 0
                        return False
                    if nums[i] == mid:
                        _sum = 0
                    else:
                        _sum = nums[i]
            size -= 1
            if size < 0:
                return False
            return True
        ans = float("inf")
        while(left <= right):
            mid = (left + right)//2
            if check(mid):
               
                ans = min(ans,mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans if ans != float("inf") else 1
