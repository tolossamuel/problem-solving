class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = Counter(s)
        counter = 0
        odd = 0
        print(dic)
        for key in dic:
            counter += dic[key] if dic[key]%2 == 0 else dic[key] - 1
            odd = max(odd,dic[key]) if dic[key]%2 == 1 else odd
        # print(odd)
        if odd > 0:
            counter += 1
        return counter


