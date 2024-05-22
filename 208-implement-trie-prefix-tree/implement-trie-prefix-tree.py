class NewTrie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
class Trie:

    def __init__(self):
        self.trie = NewTrie()
    def insert(self, word: str) -> None:
        cur = self.trie
        for s in word:
            t = ord(s)%97
            if not cur.children[t]:
                cur.children[t] = NewTrie()
            cur = cur.children[t]
        cur.is_end = True


    def search(self, word: str) -> bool:
        cur = self.trie
        for s in word:
            t = ord(s)%97
            if not cur.children[t]:
                return False
            cur = cur.children[t]
        if not cur.is_end:
            return False
        return True
    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for s in prefix:
            t = ord(s)%97
            if not cur.children[t]:
                return False
            cur = cur.children[t]
       
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)