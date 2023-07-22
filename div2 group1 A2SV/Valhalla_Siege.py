n, q = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
k = list(map(int, input().strip().split()))
summ = []
cur = 0
for i in a:
    cur += i
    summ.append(cur)
def find_loc(l, val, r, nums, target):
    l0 = l
    while l < r:
        mid = (l + r) // 2
        summ = nums[mid] - nums[l0] + val
        if summ <= target:
            l = mid + 1
        else:
            r = mid
    if nums[l] - nums[l0] + val > target:
        return l, nums[l] - nums[l0] + val - target
    else:
        return l + 1, nums[0]
st = 0
cur = summ[0]
for i in k:
    loc, cur = find_loc(st, cur, n-1, summ, i)
    if loc == n:
        print(n)
        st = 0
    else:
        print(n-loc)
        st = loc