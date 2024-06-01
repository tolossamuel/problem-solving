"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        start = deque([root])
        level = 0
        while(start):
            n = len(start)
            for _ in range(n):
                cur = start.popleft()
                for child in cur.children:
                    start.append(child)
            level += 1
        return level