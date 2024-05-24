class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = Trie()
    def insert(self,word):
        cur = self.root
        for x in word:
            if x not in cur.children:
                cur.children[x] = Trie()
            cur = cur.children[x]
        cur.is_end = True
    def find(self,word):
        index = 0
        cur = self.root
        for x in word:
            if x in cur.children:
                cur = cur.children[x]
            else:
                return len(word)
            if cur.is_end:
                return index
            index += 1
        return index
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for x in dictionary:
            self.insert(x)
        ans = []
        sentence = sentence.split(" ")
        for x in sentence:
                index = self.find(x)
                ans.append(x[:index+1])
        ans = " ".join(ans)
        return ans