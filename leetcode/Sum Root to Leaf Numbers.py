# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global ans
        ans = 0
        def sum_root(node, var):
            if node is None:
                return
            var = var * 10 + node.val
            if node.left is None and node.right is None:
                global ans
                ans += var
                return
            sum_root(node.left, var)
            sum_root(node.right, var)
        
        if root is None:
            return 0
        else:
            sum_root(root, 0)
            return ans