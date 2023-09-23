def dfs(beginning, graph, last):
    stack = [(beginning, None)]
    visited = set()
    while stack:
        node, parent = stack[-1]
        if node not in visited:
            visited.add(node)
            count = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node))
            if len(graph[node]) == 1 and parent is not None:
                count = 1
            last[node] = count
        else:
            count = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    count += last[neighbor]
            if count == 0: count = 1
            last[node] = count
            stack.pop()
    return last[beginning]


def counter_leaf(n, tree):
    graph = [[] for _ in range(n + 1)]
    leaf_count = [0] * (n + 1)

    for u, v in tree:
        graph[u].append(v)
        graph[v].append(u)

    dfs(1, graph, leaf_count)
    return leaf_count

def answer(t, test_cases):
    for _ in range(t):
        n, tree, q, assumptions = test_cases[_]

        vers = counter_leaf(n, tree)

        for apples in assumptions:
            print(vers[apples[0]]*vers[apples[1]])

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    tree = []

    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree.append((u, v))

    q = int(input())
    assumptions = []

    for _ in range(q):
        xi, yi = map(int, input().split())
        assumptions.append((xi, yi))

    test_cases.append((n, tree, q, assumptions))

answer(t, test_cases)