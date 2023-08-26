class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        visited = []
        def dfs (path, directions):
            if directions == len(graph)-1:
                visited.append(path + [directions])
            else:
                for v in graph[directions]:
                    dfs(path+[directions], v)
        dfs([],0)
        return visited