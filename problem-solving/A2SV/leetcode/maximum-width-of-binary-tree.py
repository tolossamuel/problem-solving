# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def travel(self,node):

        if not node:
            return 
        max_width = 0
        queue = deque([(node,0)])
        while(queue):
            size = len(queue)
            _, left_position = queue[0]
            for i in range(size):
                current_node,pos = queue.popleft()
                if current_node.left:
                    queue.append((current_node.left, 2 * pos))

                if current_node.right:
                    queue.append((current_node.right, 2 * pos + 1))
            current_width = pos - left_position + 1
            max_width = max(max_width, current_width)
        return  max_width
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.travel(root)
        