t = int(input())

while t > 0:
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    br = list(map(int, input().split()))

    ar.sort()
    br.sort()

    res = 0
    i = 0
    j = n - 1
    p = 0

    while p < k and br[p] == 1:
        res += 2 * ar[j]
        j -= 1
        p += 1

    q = k - 1
    while q >= p:
        res += ar[j] + ar[i]
        j -= 1
        i += 1
        br[q] -= 2
        

        i += br[q]

        q -= 1

    print(res)
    t -= 1
