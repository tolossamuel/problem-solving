class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        stack = []
        _sum = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                _sum += customers[i]
            else:
                stack.append([customers[i],i])
       
        right = 0
        left = 0
        _max= _sum
        while(right < len(stack)):
            while(stack and  (stack[right][1] - stack[left][1]) >= minutes):
                _sum -= stack[left][0]
                left += 1
            _sum += stack[right][0]
            _max = max(_max,_sum)
            right += 1
        return _max
