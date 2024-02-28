# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def travel(self,node):
        if not node:
            return 
        self.travel(node.left)
        self.ans.append(node.val)
        self.travel(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       
        self.travel(root)
        self.ans.sort()
        return self.ans[k-1]