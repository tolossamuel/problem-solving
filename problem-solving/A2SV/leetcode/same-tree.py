# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travel(self,node: Optional[TreeNode], node2: Optional[TreeNode]):
        if bool(node) != bool(node2):
            return False
        if not node and not node2:
            return True
        if node.val != node2.val:
            return False
        return self.travel(node.right,node2.right) and self.travel(node.left,node2.left)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.travel(p,q)
            
       