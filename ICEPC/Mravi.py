import math
n = int(input())
a, b, c, s = 0, 0, 0, 0
ss = False
k = 0.0
adj = [[] for _ in range(1003)]
edges = [(0, False) for _ in range(1003)]
dist = [0.0 for _ in range(1003)]
def dfs(x):
    global k, c, ss
    for v in adj[x]:
        k = dist[x]
        c = edges[v[1]][0]
        ss = edges[v[1]][1]
        if ss:
            k = math.sqrt(k)
        k = k * 100.0 / c
        dist[v[0]] = max(dist[v[0]], k)
        dfs(v[0])

leaves = []
for i in range(n - 1):
    a, b, c, s = map(int, input().split())
    a -= 1
    b -= 1
    adj[b].append((a, i))
    edges[i] = (c, s)

root = 0
dist = [0.0] * n

values = list(map(int, input().split()))
for i in range(n):
    a = values[i]
    if a != -1:
        leaves.append(i)
        dist[i] = a
    if not adj[i]:
        root = i

for leaf in leaves:
    dfs(leaf)

print(f"{dist[root]:.4f}")
