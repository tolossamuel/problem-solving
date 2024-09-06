# Problem: C - Avoid Trygub - https://codeforces.com/gym/543431/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = list(s)
    s.sort()
    s = "".join(s)
    print(s)