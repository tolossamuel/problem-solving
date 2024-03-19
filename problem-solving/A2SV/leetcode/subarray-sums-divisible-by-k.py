class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        counter = 0
        _sum = 0

        for num in nums:
            _sum = ((_sum + num) % k)
            if _sum in dic:
                counter += dic[_sum]
            dic[_sum]  = dic.get(_sum,0) + 1
        return counter
