n = int(input())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
diff = [0] * n

for i in range(n):
    diff[i] = num1[i] - num2[i]

diff.sort()

total = 0
b = 0
x = n - 1

while x >= b:
    while b < x and diff[b] + diff[x] <= 0:
        b += 1
    total += max(0, x - b)
    x -= 1

print(total)