# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        hash = defaultdict(list)
        for x in nums:
            _sum = 0
            curr = str(x)
            for y in curr:
                _sum *= 10
                _sum += mapping[int(y)]
            hash[_sum].append(int(x))
        key = list(hash.keys())
        key.sort()
        ans = []
        for x in key:
            ans += hash[x]

        return ans