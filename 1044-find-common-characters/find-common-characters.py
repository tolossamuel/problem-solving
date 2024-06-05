class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = Counter(words[0])
        removed = set()
        for x in words[1:]:
            checker = Counter(x)
            keys = dic.keys()
            for key in dic:
                if key not in checker:
                    removed.add(key)
                else:
                    dic[key] = min(dic[key],checker[key])
       
        for x in removed:
            dic.pop(x)
        ans = []
        for key in dic:
            ans += [key]*dic[key]
        return ans
            