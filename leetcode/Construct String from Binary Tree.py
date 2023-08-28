# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not(root):
            return ' '

        string = str(root.val)
        if root.left and root.right:
            string += '(' + self.tree2str(root.left) + ")(" + self.tree2str(root.right) +')'
        elif root.right:
            string += "()(" + self.tree2str(root.right) + ")"
        elif root.left:
            string += "(" + self.tree2str(root.left) + ")"
        return string
        
        