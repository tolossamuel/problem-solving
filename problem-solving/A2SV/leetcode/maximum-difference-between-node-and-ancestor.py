# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dec = []
        self.inc = []
        self.max = 0
    def travel(self,node):
        if node:
            if not self.dec or self.dec[-1].val > node.val:
                self.dec.append(node)
            if not self.inc or self.inc[-1].val < node.val:
                self.inc.append(node)
            self.max = max(self.max,abs(self.dec[-1].val - node.val), abs(self.inc[-1].val - node.val))
            self.travel(node.left)
            self.travel(node.right)
            if self.dec and self.dec[-1] == node:
                self.dec.pop()
            if self.inc and self.inc[-1] == node:
                self.inc.pop()
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
       self.travel(root)
       return self.max
