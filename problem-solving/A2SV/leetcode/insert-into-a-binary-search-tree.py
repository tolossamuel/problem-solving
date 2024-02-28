# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
    def travel(self,root,val):
        if not root:
           
            return
        if root.val < val:
            if not root.right:
                root.right = TreeNode(val)
                return 
            else:
                self.travel(root.right,val)
        if root.val > val:
            if not root.left:
                root.left = TreeNode(val)
                return 
            else:
                self.travel(root.left,val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
        self.travel(root,val)
        return root