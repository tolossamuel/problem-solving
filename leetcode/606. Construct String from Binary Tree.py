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
        def child(node,numberChild):
            
            if not node:
                return ""
            if not node.left and node.right:
                return str(node.val) + "(())"+ "("+ child(node.right,numberChild+1) + ")"
            
            return ("" + str(node.val) +"(" + child(node.left,numberChild+1) +")"+"("+ child(node.right,numberChild+1) + ")")
            
        
        ans = child(root,0)
        ans = list(ans.split("()"))
        ans = "".join(ans)
        print(ans)

        
        return ans