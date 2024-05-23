class TrieNode :
    def __init__(self) :
        self.is_end = False
        self.val = 0
        self.children = {}

 
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.visited = {}

    def insert(self, key: str, val: int) -> None:
        trie = self.root
        if key in self.visited:
            temp = val - self.visited[key]
            self.visited[key] = val
            val = temp
        else:
            self.visited[key] = val
            
        for char in key :
            if char not in trie.children:
                trie.children[char] = TrieNode()

            trie.val += val

            trie = trie.children[char]
        trie.is_end = True
        trie.val += val
    def sum(self, prefix: str) -> int:
        trie = self.root
        for char in prefix :
            if char not in trie.children:
                return 0
            trie = trie.children[char]

        return trie.val

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)