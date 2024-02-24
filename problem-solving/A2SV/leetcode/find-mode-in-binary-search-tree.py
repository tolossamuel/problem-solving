# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def dfs(node):
            
            if not node:
                return 
            
            dfs(node.left)
            dic[node.val] += 1
            dfs(node.right)
        dfs(root)
        print(dic)
        _max = 0
        ans = []
        for i in dic:
            if dic[i] == _max:
                ans.append(i)
            elif dic[i] > _max:
                _max = dic[i]
                ans = [i]
        return ans
