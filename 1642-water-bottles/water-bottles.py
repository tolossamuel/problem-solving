class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        _sum = numBottles
        while(numBottles >= numExchange):
            _sum += (numBottles//numExchange)
            numBottles = (numBottles//numExchange) + (numBottles%numExchange)
           
            
        return _sum