class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        catch = {}
        def travel(index,start):
            
            if index == len(text1):
                return 0
            if start >= len(text2):
          
                return 0
            if (index,start) in catch:
                
                return catch[(index,start)]
            ans = 0
            if text1[index] == text2[start]:
                ans = 1 + travel(index+1,start+1)
            else:
                ans = max(
                    travel(index+1,start),
                    travel(index,start+1)
                )
            catch[(index,start)] = ans

            return ans

        ans = travel(0,0)
        return ans


        # 