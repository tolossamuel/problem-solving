num = int(input())
for _ in range(num):
    x, k, q = map(int, input().split())
    arr = []
    arr.extend(map(int, input().split()))  # Read the whole line and split it
    count = 0
    i = 0
    while i < x:
        if arr[i] > q:
            i += 1
            continue
        counter = 0
        while i < x and arr[i] <= q:
            i += 1
            counter += 1
        if counter >= k:
            ab = (counter - k) + 1
            count += ((ab + 1) * ab) // 2
    print(count)
