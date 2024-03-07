class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        count = 0
        for i in range(len(nums)-1,-1,-1):
            temp = target - nums[i]
            x = bisect.bisect_right(nums,temp)
            if x == 0 and nums[x] > temp:
                continue
            
            if x >= i:
                power = i
                
                com = (pow(2,i,mod) - 1)
                if (nums[i]*2) <= target:
                    com += 1
                
                count += com
                count %= (10**9 + 7)
            else:
                
                # right = 2**(i - x)
                right = pow(2,(i-x),mod)
                # left = 2**x - 1
                left = pow(2,x,mod) - 1
                count += (left * right)
                count %= (10**9 + 7)
        count %= (10**9 + 7)
        return count