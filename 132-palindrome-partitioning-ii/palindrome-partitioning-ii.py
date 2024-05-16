class Solution:
    def minCut(self, s: str) -> int:
        catch = {}
        sr = s[::-1]
        print(sr)
        def solve(left,right):
            if right >= len(s)-1:
                x = len(s) - right-1
                y = len(s) - left
                if not (s[left:right+1] == sr[x:y]):
                    return float("inf")
                return 0
            if (left,right) in catch:
                return catch[(left,right)]
            ans = float("inf")
            x = len(s) - right-1
            y = len(s) - left

            if s[left:right+1] == sr[x:y]:
                catch[(left,right)] = min(
                    solve(right+1,right+1)+1,
                    solve(left,right+1)
                )
            else:
                catch[(left,right)] = solve(left,right+1)
            
            return catch[(left,right)]
        return solve(0,0)