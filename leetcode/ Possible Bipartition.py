class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        list_like = collections.defaultdict(list)
        for u, v in dislikes:
            u -=1
            v -= 1
            list_like[u].append(v)
            list_like[v].append(u)
        red,black,white = 0,1,2
        colors = [red]*n
        def dfs(x, y):
            list_q = collections.deque()
            colors[x] = y
            list_q.append(x)
            while len(list_q)>0:
                now = list_q.popleft()
                for i in list_like[now]:
                    if colors[i] == red:
                        if colors[now] == black:
                            colors[i] = white
                        else:
                            colors[i] = black
                        list_q.append(i)
        for i in range(n):
            if colors[i] == red:
                dfs(i,black)
        for v ,u in dislikes:
            u -= 1
            v -= 1
            if colors[u] == colors[v]:
                return False
        return True