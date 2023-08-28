n = int(input())
A1, A2 = list(map(int, input().split()))
B1, B2 = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
checker = False
if B1 < A1 and B2 < A2:
    if cx < A1 and cy < A2:
        checker = True
elif B1 > A1 and B2 < A2:
    if cx > A1 and cy < A2:
        checker = True
elif B1 > A1 and B2 > A2:
    if cx > A1 and cy > A2:
        checker = True
elif B1 < A1 and B2 > A2:
    if cx < A1 and cy > A2:
        checker = True
if checker:
    print("YES")
else:
    print("NO")
