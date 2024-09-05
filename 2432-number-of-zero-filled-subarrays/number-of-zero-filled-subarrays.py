class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        counter = 0
        _sum = 0
        for x in nums:
            if x != 0:
           
                _sum += sum(range(counter+1))
                counter = 0
            else:
                counter += 1
        _sum += sum(range(counter+1))
 
           
        return _sum
