# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = defaultdict(list)
    def travel(self,node,depth):
        if not node:
            return 
        temp = []
        # print(len(node))
        for i in node:
            if i[0].left:
                temp.append([i[0].left,i[1]-1])
                self.dic[i[1]-1].append([depth,i[0].left.val])
            if i[0].right:
                temp.append([i[0].right,i[1]+1])
                self.dic[i[1]+1].append([depth,i[0].right.val])
        node = temp        
        self.travel(node,depth + 1)
            
       
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.dic[0].append([0,root.val])
        self.travel([[root,0]],1)
        _min = min(self.dic.keys())
        _max = max(self.dic.keys())
        ans = []
        for i in range(_min,_max+1):
            self.dic[i].sort()
            temp = []
            for y in self.dic[i]:
                temp.append(y[1])
            ans.append(temp)
        return ans