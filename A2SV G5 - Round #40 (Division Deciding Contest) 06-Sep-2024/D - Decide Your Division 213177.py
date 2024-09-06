# Problem: D - Decide Your Division - https://codeforces.com/gym/543431/problem/D

def solve(n):
    start = 1
    opperation = 0
    
    while(n > 1):
        if n%2 == 0:
            n //= 2
            opperation += 1
        elif (n%3) == 0:
            n *= 2
            n //= 3
            opperation += 1
        elif (n%5) == 0:
            n *= 4
            n //= 5
            opperation += 1
        else:
            opperation = -1
            break
        
    print(opperation)
t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
          