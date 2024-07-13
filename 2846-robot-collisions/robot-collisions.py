class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        left = 0
        arr = sorted(list(zip(positions,healths,directions)))

        while(left < len(arr)):
            if arr[left][2] == "L":
                cur = arr[left][1]
                while(stack and stack[-1][1] < cur and stack[-1][2] == "R"):
                    stack.pop()
                    cur -= 1
                if not stack or stack[-1][2] == "L":
                    stack.append([arr[left][0],cur,arr[left][2]])
                elif stack[-1][1] == cur:
                    stack.pop()
                else:
                    stack[-1][1] -= 1
            else:
                stack.append([arr[left][0],arr[left][1],arr[left][2]])
            
            left += 1
        ans = {stack[x][0] : stack[x][1] for x in range(len(stack))}
        val = []
        for x in positions:
            if x in ans:
                val.append(ans[x])
        return val
            
