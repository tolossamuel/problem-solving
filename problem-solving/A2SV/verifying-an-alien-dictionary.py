class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dict = {c: i for i, c in enumerate(order)}
        sorted_words = sorted(words, key=lambda x: [order_dict[c] for c in x])
        if words == sorted_words:
            return True
        else:
            return False