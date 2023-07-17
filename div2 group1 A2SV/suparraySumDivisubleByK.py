class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        remainder_freq = {0: 1}
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum in remainder_freq:
                count += remainder_freq[prefix_sum]
            remainder_freq[prefix_sum] = remainder_freq.get(prefix_sum, 0) + 1

        return count
