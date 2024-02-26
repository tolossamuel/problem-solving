class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = Counter(s)
        set1 = set()
        set2 = set()
        x = 0
        ans = []
        for i in range(len(s)):
            set1.add(s[i])
            dic[s[i]] -= 1
            if dic[s[i]] == 0:
                set2.add(s[i])
            if set1 == set2:
                ans.append(i-x+1)
                x = i+1
                set1 = set()
                set2 = set()
        return ans

            