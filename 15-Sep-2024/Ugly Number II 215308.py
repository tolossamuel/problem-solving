# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2,3,5]
        primeNumber = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            curr = heappop(primeNumber)
            for prime in primes:
                new_ugly = curr * prime
                if new_ugly not in visited:
                    heappush(primeNumber, new_ugly)
                    visited.add(new_ugly)
                    
        return curr