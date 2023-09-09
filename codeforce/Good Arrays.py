num = int(input())
while num > 0:
    num -=1
    n, a = int(input()), input()
    ans, sum_of, m = 0, 0, {}
    for c in a:
        sum_of += (int(c) - 1)
        if sum_of == 0:
            ans += 1
        ans += m.get(sum_of, 0)
        m[sum_of] = m.get(sum_of, 0) + 1
    print(ans)