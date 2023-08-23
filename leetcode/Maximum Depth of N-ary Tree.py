"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        stack = []
        if root:
            stack.append((root, 1))
        deepth = 0
        for (node,level) in stack:
            deepth = level
            for child in node.children:
                stack.append((child, level+1))
        return deepth
