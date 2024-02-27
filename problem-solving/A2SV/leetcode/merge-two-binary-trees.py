# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travel(self,node1 : Optional[TreeNode], node2 : Optional[TreeNode]):
        if not node2:
            return 
        if  not node1.left and node2.left:
            node1.left = TreeNode(0)
        if not node1.right and node2.right:
            node1.right = TreeNode(0)
        self.travel(node1.left,node2.left)
        
        node1.val += node2.val
        
        self.travel(node1.right,node2.right)
        
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        self.travel(root1,root2)
        return root1