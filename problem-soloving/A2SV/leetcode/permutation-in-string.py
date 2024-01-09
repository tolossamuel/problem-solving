class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        charS1 = Counter(s1)
        charS2 = Counter(s2[:len_s1-1])
        j = 0
        for i in range(len_s1-1, len_s2):
            charS2[s2[i]]+=1
            if charS1 == charS2:
                return True
            charS2[s2[j]]-=1
            if charS2[s2[j]]==0:
                del charS2[s2[j]]
            j += 1
        return False