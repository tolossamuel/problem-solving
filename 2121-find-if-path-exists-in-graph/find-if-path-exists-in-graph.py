class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        for i in edges:
            dic[i[0]].append(i[1])
            dic[i[1]].append(i[0])
        visited = set()
        catch = {}
        def find(n):
            if n == destination:
                return True
            for i in dic[n]:
                if i  in visited:
                    continue
                visited.add(n)
                res = find(i)
                if res:
                    return res
            return False
        return find(source)
       

