# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node = None
    def travel(self,numbers : List[int],node):
        if not numbers and not node:
            return node
        x = len(numbers)//2
        node.val = numbers[x]
        if numbers[:x]:
            node.left = TreeNode(numbers[:x])
        if numbers[x+1:]:
            node.right = TreeNode(numbers[x:])
        self.travel(numbers[:x],node.left)
        self.travel(numbers[x+1:],node.right)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        node = TreeNode()
        self.travel(nums,node)
        return node