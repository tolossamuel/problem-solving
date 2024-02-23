class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        dec = deque(range(len(deck)))
        for card in deck:
            result[dec.popleft()] = card
            if dec:
                dec.append(dec.popleft())
        return result