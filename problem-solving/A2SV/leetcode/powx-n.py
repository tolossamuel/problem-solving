class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 != 0:
                return base * func(base * base, (exponent - 1) // 2)
            else:
                return func(base * base, exponent // 2)

        ans = func()

        return float(ans) if n >= 0 else 1 / ans