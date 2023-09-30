def main():
    mod = 10**9 + 7
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr1 = [0] * (n + 1)
        b1 = True

        for i in range(n):
            if arr[i] > n:
                b1 = False
                continue
            arr1[arr[i] - 1] += 1

        for i in range(n - 1, -1, -1):
            arr1[i] += arr1[i + 1]
            if arr1[i] != arr[i]:
                b1 = False

        if b1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
