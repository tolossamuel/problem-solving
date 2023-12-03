from collections import Counter


class Solution(object):
    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def calc(s):
            res = 0
            v = len(s)
            for i in range(1, 27):
                if i * k > v: break
                l = i * k
                cnt = Counter(s[:l])
                freq = Counter(cnt.values())
                
                if freq[k] == i: res += 1
                
                for idx in range(v - l):
                    freq[cnt[s[idx]]] -= 1
                    cnt[s[idx]] -= 1
                    freq[cnt[s[idx]]] += 1

                    freq[cnt[s[idx+l]]] -= 1
                    cnt[s[idx+l]] += 1
                    freq[cnt[s[idx+l]]] += 1

                    if freq[k] == i: res += 1
            return res
        
        idx = 0
        ans = 0
        n = len(word)
        for i in range(1, n):
            if abs(ord(word[i]) - ord(word[i-1])) > 2:
                ans += calc(word[idx:i])
                idx = i
        ans += calc(word[idx:])
        return ans