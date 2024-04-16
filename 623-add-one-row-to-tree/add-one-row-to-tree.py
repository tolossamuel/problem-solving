# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def travel(node,n):
            queue = deque(node)
            level = 1
            while(queue):
                x = len(queue)
                for i in range(x):
                    curr = queue.popleft()
                    if (level+1) == n:
                        left_child = None if not curr.left else curr.left
                        right_child = None if not curr.right else curr.right
                        curr.left = TreeNode(val,left_child)
                        curr.right = TreeNode(val,None,right_child)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                if (level+1) == n:
                    return
                level += 1
        if depth == 1:
            new_node = TreeNode(val,root)
            return new_node
        travel([root],depth)
        return root
