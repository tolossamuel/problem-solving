# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return []
        
            left = dfs(node.left)
            right = dfs(node.right)
            for i in range(len(left)):
                for j in range(len(right)):
                    if left[i] + right[j] <= distance:
                        
                        ans += 1
                left[i] += 1
            if not left and not right:
                left = [1]

            for i in range(len(right)):
                right[i] += 1
          
            return left+right
        dfs(root)
      
        return ans

            
