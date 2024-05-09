class Solution:
    def fib(self, n: int) -> int:
        catch = {}
        def fib(x):
            if x <= 1:
                return x
            if x in catch:
                return catch[x]
            res = fib(x-1) + fib(x-2)
            catch[x] = res
            return res
        return(fib(n))