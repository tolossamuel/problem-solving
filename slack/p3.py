def solve():
    n, a,b = list(map(int, input().split()))
    if n == a == b:
        return 'Yes'

    if a+b+2 <= n:
        return 'Yes'
    else:
        return 'No'


for t in range(0, int(input())):
    print(solve())