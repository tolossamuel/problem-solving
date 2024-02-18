class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        checker = defaultdict(int)
        counter = 0
        for i in range(len(answers)):
            if answers[i] == 0:
                counter  += 1
            elif answers[i] not in dic or checker[answers[i]] == 0:
                dic[answers[i]] = 1
                counter += (answers[i]+1)
                checker[answers[i]] = answers[i]
            else:
                checker[answers[i]] -= 1
        return counter
