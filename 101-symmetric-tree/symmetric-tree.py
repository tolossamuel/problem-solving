# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def travel(root1,root2):
            if bool(root1)!= bool(root2):
                return False
            if not root1 and  not root2:
                return True
            if root1.val != root2.val:
                return False
            return travel(root1.left,root2.right) and travel(root1.right,root2.left)
           
           
        return travel(root.left,root.right)
        