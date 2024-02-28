# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.store = set()
        self.ans = None
    
    def travel(self,root: 'TreeNode',p : 'TreeNode',q : 'TreeNode'):
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        if (min(p.val,q.val) < root.val) and max(p.val,q.val) > root.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.travel(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.travel(root.right,p,q)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.travel(root,p,q)
        