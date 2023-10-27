class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        prefix_mod_k = {0: -1}

        cumulative_sum = 0
        for i, num in enumerate(nums):
            cumulative_sum += num
            if k != 0:
                cumulative_sum %= k
            if cumulative_sum in prefix_mod_k:
                if i - prefix_mod_k[cumulative_sum] > 1:
                    return True
            else:
                prefix_mod_k[cumulative_sum] = i

        return False

# 23, 25, 31,35,42