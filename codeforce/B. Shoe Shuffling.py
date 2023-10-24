def solve():
    n = int(input())
    m = {}
    v = list(map(int, input().split()))
    ans = []

    for i in range(n):
        if v[i] not in m:
            m[v[i]] = 1
        else:
            m[v[i]] += 1

    for x in m:
        if m[x] == 1:
            print(-1)
            return

    i = 0
    while i < n:
        pos = [i + 1]
        j = i + 1

        while j < n and v[j] == v[i]:
            pos.append(j + 1)
            j += 1

        i = j
        ans.append(pos[-1])

        for k in range(len(pos) - 1):
            ans.append(pos[k])

    print(*ans)

def main():
    speed = 1
    test_cases = int(input())
    for _ in range(test_cases):
        solve()

if __name__ == "__main__":
    main()
