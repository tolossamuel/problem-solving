# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        checker = set(allowed)
        # print(checker)
        counter = 0
        for x in words:
            for y in x:
                if y not in checker:
                    counter -= 1
                    break
            counter += 1
        return counter
