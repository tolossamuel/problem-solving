# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = None
    def travel(self,root : Optional[TreeNode], val : int):
        if not root:
            return 
        self.travel(root.left,val)
        if root.val == val:
            self.ans = root
            return self.ans
        self.travel(root.right,val)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.travel(root,val)
        return self.ans
        