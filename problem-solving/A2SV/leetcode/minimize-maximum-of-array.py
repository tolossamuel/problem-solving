class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _max = nums[0]
        _sum = nums[0]
        for i in range(1,len(nums)):
            _sum += nums[i]
            if nums[i] > _max:
                re = _sum % (i + 1)
                
                diff =( _sum // (i + 1))
                diff += 1 if re >0 else 0
                _max = max(_max, (diff))
        return _max
