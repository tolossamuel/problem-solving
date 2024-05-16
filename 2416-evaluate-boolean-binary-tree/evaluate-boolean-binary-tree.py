# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def travel(node):
            if not node:
                return True
            left_child = travel(node.left)
            right_child = travel(node.right)
            if node.val == 2:
                return left_child or right_child
            if node.val == 3:
                return left_child and right_child
            if node.val:
                return True
            return False
        return travel(root)
