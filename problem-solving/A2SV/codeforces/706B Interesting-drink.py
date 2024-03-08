from collections import*
import bisect
n = int(input())
l = list(map(int,input().split()))
l.sort()
q = int(input())
ans = []
for _ in range(q):
    p = int(input())
    number = bisect.bisect_right(l,p)
    if number >= len(l):
        ans.append(len(l))
    elif p < l[number]:
        ans.append(number)
    else:
        ans.append(number + 1)
for i in ans:
    print(i)