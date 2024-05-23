class TrieNode :
    def __init__(self) :
        self.is_end = False
        self.children = {}
class Solution:
    def __init__(self) :
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        trie = self.root
        for char in word :
            if char not in trie.children:
                trie.children[char] = TrieNode()
            trie = trie.children[char]

        trie.is_end = True
    def longestWord(self, words: List[str]) -> str:
        for x in words:
            self.insert(x)
        
        queue = deque([[self.root,""]])
        ans = ""
        while(queue):
            n = len(queue)
            for _ in range(n):
                cur,word = queue.popleft()
             
                if cur.is_end:
                    if len(ans) < len(word):
                        ans = word
                    elif len(ans) == len(word):
                        ans = min(ans,word)
                for x in cur.children:
                    if cur.children[x].is_end:
                        queue.append([cur.children[x],word+x])
    
        return ans