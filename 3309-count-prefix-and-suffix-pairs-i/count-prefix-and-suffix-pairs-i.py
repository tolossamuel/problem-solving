class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        for x in range(len(words)):
            words[x] = [len(words[x]),words[x]]
        
        counter = 0
        for x in range(len(words)):
            w = words[x][1]
            for y in range(x+1,len(words)):
                w2 = words[y][1]
                if w == w2[:len(w)] and w == w2[len(w2)-len(w):]:
                    counter += 1

                
        return counter