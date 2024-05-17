# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def travel(node):
            if not node:
                return None,True
            left,left_deleted= travel(node.left)
            right,right_deleted = travel(node.right)
            node.left = left
            node.right = right
            if left_deleted and right_deleted and node.val == target:
                return None,True
            
            return node,False
        travel(root)
        if root and not root.left and not root.right and root.val == target:
            return None
        return root