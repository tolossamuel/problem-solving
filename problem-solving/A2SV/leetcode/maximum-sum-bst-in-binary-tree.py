# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._max = 0
    def travel(self,node):
        if not node:
            return [1,0,None,None]
        left = self.travel(node.left)
        right = self.travel(node.right)
        if ((left[0] == 2 and left[3] < node.val) or left[0] == 1) and  ((right[0] == 2 and right[2] > node.val) or right[0] == 1):
            size = node.val + left[1] + right[1]
            self._max = max(size,self._max)
            left_b = left[2] if left[2] != None else node.val
            right_b = right[3] if right[3] != None else node.val
            return [2,size,left_b,right_b]
        return [0,None,None,None]
        
        
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.travel(root)
        # print(self.ans,self._max)
        return self._max