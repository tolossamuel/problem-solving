n,m=list(map(int,input().split()))
a = list(map(int,input().split()))
q = [0]*m
dist = [0] * (n+1)
for i in range(m):
    l,r = list(map(int,input().split()))
    q[i] = (l,r)
    dist[l-1] += 1
    dist[r] -= 1
d = [(dist[0],0)]
for i in range(1,n):
    dist[i] += dist[i-1]
    d.append((dist[i],i))
d.sort(key=lambda item:item[0],reverse=True)
a.sort(reverse=True)
final = [0]*n
for i in range(n):
    final[d[i][1]] = a[i]
prefixSum = [0]
for i in range(n):
    prefixSum.append(prefixSum[-1] + final[i])
result = 0
for j in q:
    result += prefixSum[j[1]] - prefixSum[j[0]-1]
print(result)
