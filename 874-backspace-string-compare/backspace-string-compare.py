class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left = []
        for i in s:
            if i == "#":
                if left:
                    left.pop()
            else:
                left.append(i)
        right = []
        for i in t:
            if i == "#":
                if right:
                    right.pop()
            else:
                right.append(i)
        return left == right
