# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """    
        global ans
        def dfs(root):
            global ans
            if not root:
                return
            
            if parent[root] and parent[parent[root]]:
                if parent[parent[root]].val%2==0:
                    ans+=root.val

            if root.left:
                parent[root.left]=root
            if root.right:
                parent[root.right]=root
            
            dfs(root.left)
            dfs(root.right)
        
        ans=0
        parent=defaultdict(lambda : None)
        dfs(root)
        
        return ans