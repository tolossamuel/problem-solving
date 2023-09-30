import sys
mod = 1000000007

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        ans = 0
        for i in range(n - 1):
            if i == n - 2:
                ans += 1
                break
            else:
                if s[i] == s[i + 2]:
                    continue
                else:
                    ans += 1
        print(ans)

if __name__ == "__main__":
    main()
