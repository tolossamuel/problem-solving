# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return [root]
        start = root.val
        ans = []
        to_delete = set(to_delete)
        new_root = root

        def travel(node,new_root):
            nonlocal start
            nonlocal ans
            if not node:
                return None
            new_root.left = travel(node.left,new_root.left)
            new_root.right = travel(node.right,new_root.right)
            
            if node.val in to_delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                node = None
                return None
            return node


            
        travel(root,new_root)
        if new_root and new_root.val not in to_delete:
            ans.append(new_root)
        return ans