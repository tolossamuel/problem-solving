# Problem: Small GCD - https://codeforces.com/contest/1900/problem/D

from sys import stdin, stdout

def pr(out):
    return stdout.write(f"{out}\n")


def ver_in():
    return stdin.readline()


def hor_in():
    return list(map(int, stdin.readline().split()))

if __name__ == "__main__":
    N = 10**5 + 10
    div = [[] for _ in range(N)]
    for i in range(1, N):
        for j in range(i, N, i):
            div[j].append(i)

    for i in range(N):
        div[i].sort(reverse=True)

    cnt = [0] * N
    tmp = [0] * N

    def solve():
        n = int(input())
        nums = hor_in()
        nums.sort()
        ans = 0
        rem = n
        for num in nums:
            rem -= 1
            for d in div[num]:
                val = cnt[d] - tmp[d]
                for d2 in div[d]:
                    tmp[d2] += val
                ans += d * val * rem

            for d in div[num]:
                for d2 in div[d]:
                    tmp[d2] = 0

            for d in div[num]:
                cnt[d] += 1
        for num in nums:
            for d in div[num]:
                cnt[d] = 0
        print(ans)

    t = int(ver_in())
    for _ in range(t):
        solve()