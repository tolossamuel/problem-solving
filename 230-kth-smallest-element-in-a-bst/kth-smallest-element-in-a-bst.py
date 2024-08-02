# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        counter = 0
        def dfs(current):
            nonlocal ans
            nonlocal counter
            if not current:
                return None
            dfs(current.left)
            counter += 1
            if counter == k:
                ans = current.val
            dfs(current.right)
            return current
        dfs(root)
        return ans