# 580C-Kefa and Park

def dfs():
    list1 = [(li[0], 0, 0)]
    sum_checker = 0
    while list1:
        checker = True
        count, v, p = list1.pop(0)
        for j in graph[v]:
            if j == p:
                continue
            checker = False
            if li[j] == 0:
                list1.append((0, j, v))
            elif count + 1 <= m:
                list1.append((count + 1, j, v))
        if checker:
            sum_checker += 1

    return sum_checker

if __name__ == '__main__':
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    graph = [[] for i in range(n)]
    for i in range(n - 1):
        s, d = map(int, input().split())
        graph[s - 1].append(d - 1)
        graph[d - 1].append(s - 1)
    # print(graph)
    print(dfs())