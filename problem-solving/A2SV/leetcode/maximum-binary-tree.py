# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.numbers = []
    def creat(self,node,temp):
        if not temp:
            return 
        _max = max(temp)
        index = temp.index(_max)
        node.val = _max
        if temp[:index]:
            node.left = TreeNode(temp[:index])
        if temp[index+1:]:
            node.right = TreeNode(temp[index+1:])
        self.creat(node.left,temp[:index])
        self.creat(node.right,temp[index+1:])
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        node = TreeNode()
        self.creat(node,nums)
        return node
