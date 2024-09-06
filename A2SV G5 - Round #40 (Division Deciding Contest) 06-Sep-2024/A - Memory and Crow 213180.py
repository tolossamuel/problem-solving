# Problem: A - Memory and Crow - https://codeforces.com/gym/543431/problem/A

n = int(input())

l = list(map(int,input().split()))
b = [l[-1]]

odd = b[0] if (n-1)%2 == 1 else 0
even = b[0] if (n-1)%2 == 0 else 0

for i in range(len(l)-2,-1,-1):
    if (i%2 == 0):
        curr = l[i] + odd - even
        even += curr
        b.append(curr)
    else:
        curr = l[i] - odd + even

        odd += curr
        b.append(curr)

    
        
print(*b[::-1])
