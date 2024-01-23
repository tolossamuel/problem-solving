class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def compare(string,k):
            x = 0
            y = 0
            index = deque()
            ans = 0
            counter = 0
            while(y < len(s) or len(index) > k):
                if counter > k:
                    
                    ans = max(ans,(y-x-1))
                    x = index.pop()+1
                    counter -= 1
                    
                else:
                    if s[y] != string:
                        index.appendleft(y)
                        counter += 1
                    y += 1
    
            ans = max(ans,(y-x))
            
            return ans
        # print(compare("B",k),compare("A",k))
        ANS  = 0
        x = set(s)
        for i in x:
            print(i)
            ANS = max(ANS,compare(i,k))
        return ANS


