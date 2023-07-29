from bisect import bisect_right
def binary_search(l_p, m, l, h):
    if l >= h:
        return (l + 1) if l_p[l] <= m else l
    mid = (h + l) // 2
    if l_p[mid] >= m:
        return binary_search(l_p, m, l, mid)
    elif l_p[mid] < m:
        return binary_search(l_p, m, mid + 1, h)
_ = input()
l_p = list(map(int, input().split()))
l_p.sort()
for _ in range(int(input())):
    t = 0
    m = int(input())
    print(bisect_right(l_p, m))