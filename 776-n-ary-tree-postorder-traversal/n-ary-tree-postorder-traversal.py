"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []



        def dfs(start):
            if not start:
                return 
            for x in start.children:
                dfs(x)
                arr.append(x.val)
        dfs(root)
        if root:
            arr.append(root.val)
        return arr