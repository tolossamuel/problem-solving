class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = Counter(answers)
        ans = 0
        for i in answers:
            rem = 0
            diff = 1
            if dic[i] > (i+1):
                diff = dic[i]
                rem = 1 if diff%(i+1) > 0 else 0
                diff //= (i+1)
            ans += (diff*(i+1) + (rem*(i+1))) if dic[i] > 0 else 0
            dic[i] = 0
        return ans