# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        if len(start) < len(goal):
            start = "0"*(len(goal)-len(start)) + start
        elif len(goal) < len(start):
            goal  = "0"*(len(start) - len(goal)) + goal
        for x in range(len(goal)):
            if start[x] != goal[x] :
                ans += 1
        return ans