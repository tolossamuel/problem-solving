def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        ar = list(map(int, input().split()))
        prf = [0] * (n + 2)
        prf[0] = 0
        for i in range(n):
            prf[i + 1] = prf[i] + ar[i] % 2
        
        for _ in range(q):
            l, r, k = map(int, input().split())
            x = (prf[r] - prf[l - 1]) % 2
            if k % 2:
                tmp = r - l + 1
                if tmp % 2:
                    if not x:
                        print("NO" if prf[n] % 2 else "YES")
                    else:
                        print("NO" if prf[n] % 2 == 0 else "YES")
                else:
                    if x:
                        print("NO" if prf[n] % 2 else "YES")
                    else:
                        print("NO" if prf[n] % 2 == 0 else "YES")
            else:
                if x:
                    print("NO" if prf[n] % 2 else "YES")
                else:
                    print("NO" if prf[n] % 2 == 0 else "YES")

if __name__ == "__main__":
    main()
