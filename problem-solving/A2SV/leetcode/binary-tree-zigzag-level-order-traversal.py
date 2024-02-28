# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def travel(self,parent):
        if not parent:
            return 
        
        temp = []
        exist = []
        for i in parent:
            if i:
                exist.append(i.val)
            if i and i.left:
                temp.append(i.left)
            if i and i.right:
                temp.append(i.right)
        if len(self.ans)%2 == 0 and exist:
            self.ans.append(exist)
        elif exist:
            self.ans.append(exist[::-1])
        parent = temp
        self.travel(parent)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.travel([root])
        return self.ans