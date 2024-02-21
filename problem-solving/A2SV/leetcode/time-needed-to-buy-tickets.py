class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        for i in range(len(tickets)):
            if i <= k:
                counter += min(tickets[i],tickets[k])
            else:
                counter += min(tickets[i],tickets[k]-1)
            
        return counter