class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        q = deque([target])
        level = 0
        visited = set([target])
        while(q):
            l = len(q)
            for _ in range(l):
                curr = q.popleft()
                # print(curr)
                if curr == "0000":
                    return level
             
                # print(curr)
                for i in range(4):
                    x = curr
                    # print(x)
                    r = int(x[i]) - 1
                    r = 9 if r < 0 else r
                    r = str(r)
                    x = x[:i] + r + x[i+1:]
                    if x not in deadends and x not in visited:
                        visited.add(x)
                        q.append(x)
                    x = curr
                    r = int(x[i]) + 1
                    r = 0 if r > 9 else r
                    r = str(r)
                    x = x[:i] + r + x[i+1:]
                    if x not in deadends and x not in visited:
                        visited.add(x)
                        q.append(x)
            level += 1
        return -1

