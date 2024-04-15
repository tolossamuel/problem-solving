# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def travel(self,node,total):
        if not node:
            
            return 
        
        total *= 10
        total += node.val
        if not node.left and not node.right:
            self.ans += total

        self.travel(node.left,total)
        self.travel(node.right,total)
        # if not root.
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.travel(root,0)
        return self.ans