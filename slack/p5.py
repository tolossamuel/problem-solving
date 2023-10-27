n = int(input())
x = list(map(int, input().split()))
left = 0

pre_sum = [x[0]]
suf_sum = [x[-1]]
for i in range(1,len(x),+1):
	pre_sum.append(pre_sum[i-1]+x[i])
	suf_sum.append(x[len(x)-i-1]+suf_sum[i-1])
for i in range(len(pre_sum)):
	if n == pre_sum[i]:
		left = i+1
		break

for i in range(len(suf_sum)):
	if n == suf_sum[i]:
		if (left > i+1 or left == 0):
			left = i+1
		break
for i in range(len(x)):
	if (n == 0):
		if (left > i+1 or left == 0):
			left = i+1
		break
	if (n < 0):
		center = 0
		break
	if x[i]< x[len(x)-1-i]:
		n -= x[i]
	else:
		n -= x[len(x)-1-i]
	
if left == 0:
	print(-1)
else:
	print(left)


