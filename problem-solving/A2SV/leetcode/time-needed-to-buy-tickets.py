class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        i = 0
        while(tickets[k] != 0):
            if tickets[i%len(tickets)] != 0:
                tickets[i%len(tickets)] -= 1
                counter += 1
            i += 1
        return counter