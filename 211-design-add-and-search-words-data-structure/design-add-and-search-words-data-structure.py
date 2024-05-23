
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()
    def addWord(self, word: str) -> None:
        cur = self.root
        for x in word:
            if not x in cur.children:
                cur.children[x] = Trie()
            cur = cur.children[x]
        cur.is_end = True
    

    def search(self, word: str) -> bool:
        cur = self.root
        queue = deque([self.root])
        index = 0
        while(queue):
            n = len(queue)
            ans = False
            counter = 0
            for _ in range(n):
                cur = queue.popleft()
                if index < len(word):
                    if word[index] == ".":
                        
                        for x in cur.children:
                            queue.append(cur.children[x])
                            counter += 1

                    else:
                        if word[index] in cur.children:
                            queue.append(cur.children[word[index]])
                            counter += 1
                    
                else:
                    if cur.is_end:
                        return True
            if counter == 0:
                return False
            index += 1
     
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)