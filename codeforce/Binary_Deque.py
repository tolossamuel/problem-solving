for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    i, j, summ, ans = 0, 0, 0, -1
    while j < n:
        summ += a[j]
        while summ > s:
            summ -= a[i]
            i += 1
        if summ == s:
            ans = max(ans, j-i+1)
        j += 1
    if ans == -1:
        print(ans)
    else:
        print(n - ans)