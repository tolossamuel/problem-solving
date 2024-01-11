class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def counter(string):
            stack = deque()
            left = 0
            right = 0
            count = 0
            ans = 0
            while(right < len(answerKey)):
                if answerKey[right] == string:
                    count += 1
                    stack.appendleft(right)
                    
                    
                    if count > k:
                        ans = max(ans,(right - left))
                        
                        left = stack.pop()+1
                        count -= 1
                    right += 1
                        
                else:
                    right += 1
                # print(stack,ans)
            ans = max(ans,right-left)
            return ans
        T = counter("T")
        # print(T)
        F = counter("F")
        return max(T,F)
