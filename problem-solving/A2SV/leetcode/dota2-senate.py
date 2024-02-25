class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        winner = [senate[0]]
        size = len(senate)
        senate = list(senate)
        x = 1
        while(x < size):
            if not winner:
                winner.append(senate[x])
            elif winner[-1] != senate[x]:
                senate.append(winner.pop())
                size += 1
            else:
                winner.append(senate[x])
            x += 1
        if winner[0] == "R":
            return "Radiant"
        return "Dire"
