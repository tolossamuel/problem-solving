# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        heap  = Counter(word)
        freq = [[x,y] for y,x in heap.items()]
        freq.sort(reverse = True)
        _max = 8
        counter = 0
        current = 1
        _sum = 0
        for x,y in freq:
            _sum += (current*x)
            counter += 1
            if counter == 8:
                counter = 0
                current += 1
        return _sum

            