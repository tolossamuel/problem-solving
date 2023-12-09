# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def travel(root):
           
            if root:
            
                travel(root.left)
                ans.append(root.val)
               
                travel(root.right)
        travel(root)
        print(ans)
        return ans


        