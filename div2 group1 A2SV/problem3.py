t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    temperatures = list(map(int, input().split()))

    count = 0
    maxo = 0
    ans = 0

    for i in range(n):
        if temperatures[i] <= q:
            count += 1
        else:
            count = 0

        if count >= k:
            ans += n - i

    print(ans)
