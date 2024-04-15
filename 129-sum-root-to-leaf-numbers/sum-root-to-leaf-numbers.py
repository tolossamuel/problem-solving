# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        _sum = 0
        def travel(node,number):
            nonlocal _sum
            if not node:

                return
            travel(node.left,number + [str(node.val)])
            travel(node.right,number + [str(node.val)])
            # print(number + [str(node.val)])
            if not node.left and not node.right:
                x = int("".join(number + [str(node.val)]))
                # print(x)
                _sum += x
            

            return node
        travel(root,[])
        return _sum
