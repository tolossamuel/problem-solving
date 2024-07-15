# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        childs = set()
        val = {}
        for i in range(len(descriptions)):
            x,y,z = descriptions[i]
            if x in val:
                parent = val[x]
            else:
                parent = TreeNode(x)
                val[x] = parent
            if y in val:
                child = val[y]
            else:
                child = TreeNode(y)
                val[y] = child
            childs.add(child)
            descriptions[i] = [parent,child,z]
        head = []
        
        for x,y,z in descriptions:
            if z == 1:
                x.left = y
            else:
                x.right = y
            if x not in childs:
                head.append(x)
        # print(head)
        return  head[0]