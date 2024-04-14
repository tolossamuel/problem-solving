# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        _sum = 0
        def travel(node,child):
            nonlocal _sum
            if not node:
                return 
            travel(node.left,0)
            travel(node.right,1)
            if not node.right and not node.left and child == 0:
                _sum += node.val
                
            return node
        travel(root,-1)
        return _sum