class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {0:-1}
        _sum = 0
        zeros = 0
        for x in range(len(nums)):
            _sum += nums[x]
            dif = _sum % k
            if dif in map:
                y = map[dif]
                # print(y)
                if x - y >1:
                    return True
            if (_sum%k) not in map:
                map[_sum%k] = x
            if nums[x] == 0:
                zeros += 1
            else:
                if zeros >= 2:
                    return True
                zeros = 0
        
        if zeros >= 2:
            return True
            
        return False


