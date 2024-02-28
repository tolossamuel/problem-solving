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
    def parent(self,node,prev):
        if not node:
            return 
        node.pre = prev
        
        self.parent(node.left,node)
        self.parent(node.right,node)

    def travel(self,root: 'TreeNode',p : 'TreeNode',q : 'TreeNode'):
        if not root:
            return       
        self.travel(root.left,q,p)
        if root == p or root == q:
            temp = root
            while(temp != None):
                
                if temp.val in self.store and self.ans == None:
                   
                    self.ans = temp
                    
                self.store.add(temp.val)
                temp = temp.pre
        self.travel(root.right,q,p)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.parent(root,None)
        self.travel(root,p,q)
        return self.ans