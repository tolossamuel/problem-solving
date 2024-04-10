# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dic = defaultdict(list)
        stack = deque([root])
        while(stack):
            curr = stack.popleft()
            if curr.left:
                dic[curr.val].append(curr.left.val)
                dic[curr.left.val].append(curr.val)
                stack.append(curr.left)
            if curr.right:
                dic[curr.val].append(curr.right.val)
                dic[curr.right.val].append(curr.val)
                stack.append(curr.right)
        level = 0
        stack = deque([target.val])
        ans = []
        visited = set([target.val])
        while(stack):
            n  = len(stack)
            for _ in range(n):
            
                curr = stack.popleft()
                # print(level,dic[curr],curr)
                if level == k:
                    # print(curr,k,level)
                    ans.append(curr)
                else:
                    for i in dic[curr]:
                        # print(i)
                        if i not in visited:
                            stack.append(i)
                            visited.add(i)
            level += 1
        # print(ans)
        return ans
            