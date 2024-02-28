# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travel(self,root,key):
        if not root:
            return
        if key > root.val:
            root.right = self.travel(root.right,key)
        elif key < root.val:
            root.left = self.travel(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            min_Node = self.findmax(root.right)
            root.val = min_Node.val
            root.right = self.travel(root.right,min_Node.val)
        return root

    def findmax(self,node):
        while(node.left):
            node = node.left
        return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.travel(root,key)