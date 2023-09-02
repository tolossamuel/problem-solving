# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [root.val]

        def dfs(root):
            if not root:
                return (0)
            left_val = dfs(root.left)
            right_val = dfs(root.right)
            left_val = max(left_val,0)
            right_val = max(right_val, 0)

            result[0] = max(result[0], root.val + left_val + right_val)
            return root.val + max(left_val, right_val)
        dfs(root)
        return result[0]