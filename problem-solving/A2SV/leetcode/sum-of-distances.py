class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index = defaultdict(int)
        _sum = defaultdict(lambda: [0])
        for i in range(len(nums)):
            _sum[nums[i]].append(_sum[nums[i]][-1] + i)
        ans = []
        for i in range(len(nums)):
            left_side = abs((index[nums[i]] * i) - _sum[nums[i]][index[nums[i]]])
            right_side = 0
            right_side = abs(_sum[nums[i]][-1] - _sum[nums[i]][index[nums[i]]] - ( i * (len(_sum[nums[i]]) - (index[nums[i]] + 1))))
            
            ans.append(left_side + right_side)
            index[nums[i]] += 1
        return ans
