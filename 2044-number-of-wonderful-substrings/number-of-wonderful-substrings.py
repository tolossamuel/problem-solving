class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        arr = [0] * 1024
        ans = 0
        arr[0] = 1
        counter = 0
        for i in word:
            index = ord(i) - ord("a")
            counter ^= 1 << index
            ans += arr[counter]
            for y in range(10):
                ans += arr[counter ^ (1 << y)]
            arr[counter] += 1
        return ans