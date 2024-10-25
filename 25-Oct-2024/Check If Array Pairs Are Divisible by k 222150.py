# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod = [0]*k
        for i in arr:
            i %= k
            mod[i] += 1
        # print(arr)
        if mod[0]%2 == 1:
            return False
        for i in range(1,(k//2)+1):
            if mod[i] != mod[k-i]:
                return False
        return True
