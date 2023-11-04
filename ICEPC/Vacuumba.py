import cmath
import math

n = int(input())

for _ in range(n):
    m = int(input())
    p = complex(0, 0)
    a = math.pi / 2

    for _ in range(m):
        d, l = map(float, input().split())
        a += (d * math.pi / 180)
        p += cmath.rect(l, a)

    print(f'{p.real:.10f} {p.imag:.10f}')
