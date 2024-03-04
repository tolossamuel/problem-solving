# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.numbers = []
    def travel(self,root):
        if not root:
            return 
        self.travel(root.left)
        self.numbers.append(root.val)
        self.travel(root.right)
    def create(self,numbers,node):
        if not numbers and not node:
            return 
        x = len(numbers)//2
        node.val = numbers[x]
        if numbers[:x]:
            node.left = TreeNode(numbers[:x])
        if numbers[x+1:]:
            node.right = TreeNode(numbers[x+1:])
        self.create(numbers[:x],node.left)
        self.create(numbers[x+1:],node.right)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        node = TreeNode()
        self.travel(root)
        self.create(self.numbers,node)
        return node