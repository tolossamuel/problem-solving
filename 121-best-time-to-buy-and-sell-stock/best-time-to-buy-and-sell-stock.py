class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        amount = 0
        for i in prices:
            if not stack:
                stack.append(i)
            while(len(stack) > 1 and stack[-1] < i):
                stack.pop()
            while(stack and stack[-1] > i):
                stack.pop()
            stack.append(i)
            if len(stack) > 1:
                amount = max(amount,(stack[-1] - stack[-2]))

        return amount