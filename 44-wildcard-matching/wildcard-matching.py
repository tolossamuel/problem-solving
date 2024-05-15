class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "" and p and p[0] == "*":
            s = "*"
        elif s and not p:
            return False
        catch = {}
        def solve(left,right):
            if left >= len(s):
                if right >= len(p):
                    return True
                x = "".join(set(list(p[right:])))
                if x == "*":
                    return True
                return False
            if right >= len(p):
                return left >= len(s)
            ans = False
            if (left,right) in catch:
                return catch[(left,right)]
            if p[right] == "*":
                ans = ans or (
                    solve(left+1,right) or solve(left+1,right+1) or solve(left,right+1)
                )
            elif p[right] == "?" or s[left] == p[right]:
                ans = ans or solve(left+1,right+1)
            else:
                return False
            catch[(left,right)] = ans
            return ans
        return solve(0,0)