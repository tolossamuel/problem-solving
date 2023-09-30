import sys

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        x_values = list(map(int, input().split()))
        mp = {}
        maxi = 0
        for i in range(n):
            x = x_values[i]
            maxi += mp.get(x - i, 0)
            mp[x - i] = mp.get(x - i, 0) + 1
        print(maxi)

if __name__ == "__main__":
    main()
