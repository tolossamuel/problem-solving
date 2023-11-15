n = int(input())
l = list(map(int, input().split()))
left = 0
right = n - 1
serj = 0
dima = 0
while (left < right):
	if l[left] < l[right]:
		serj += l[right]
		right -= 1
	else:
		serj += l[left]
		left += 1
	if l[left] < l[right]:
		dima += l[right]
		right -= 1
	else:
		dima += l[left]
		left += 1
if n%2 != 0:
	serj += l[left]
print(f"{serj} {dima}")

