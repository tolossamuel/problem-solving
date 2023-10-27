class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        deck.sort()
        result = [0] * n
        indexs = deque(range(n))
        for card in deck:
            result[indexs.popleft()] = card
            if indexs:
                indexs.append(indexs.popleft())
        return result