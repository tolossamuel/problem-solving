# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target *= -1
        start = 0
        step = 0
        next_step = 1
        while(start < target):
            start += next_step
            next_step += 1
            step += 1
   
        while((start - target)%2 == 1):
            start += next_step
            step += 1
            next_step += 1
        return step
