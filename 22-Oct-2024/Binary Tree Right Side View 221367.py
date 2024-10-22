# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def travel(self,node,depth):
        if not node:
            return 
        self.travel(node.left,depth+1)
        if depth > len(self.ans):
            self.ans += [0] * (depth - len(self.ans)+1)
        elif depth == len(self.ans):
            self.ans.append(0)
        self.ans[depth] = node.val
        self.travel(node.right,depth+1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.travel(root,0)
   
        return self.ans